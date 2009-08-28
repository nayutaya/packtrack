# -*- coding: utf-8 -*-

import re
import urllib
import urllib2
from BeautifulSoup import BeautifulSoup


class PackageTrackingNumber:
  pattern = re.compile(r"^[0-9]{12}$")

  def __init__(self):
    pass

  @classmethod
  def create_check_digit(cls, body_digits):
    return str(int(body_digits) % 7)

  @classmethod
  def split_check_digit(cls, digits):
    return (digits[0:11], digits[11:12])

  @classmethod
  def is_valid(cls, digits):
    if cls.pattern.match(digits) is None: return False
    body_digits, check_digit = cls.split_check_digit(digits)
    if check_digit != cls.create_check_digit(body_digits): return False
    return True


class PackageTrackingSession:
  def __init__(self):
    self.jsession_id = None

  def setup(self):
    if self.jsession_id is None:
      first_page = self.get_first_page()
      first_info = PackageFirstPageParser.parse(first_page.content)
      self.jsession_id = first_info["jsessionid"]
    return self

  def get_first_page(self):
    return PackageFirstPage.get()

  def get_list_page(self, numbers):
    self.setup()
    return PackageListPage.get(self.jsession_id, numbers)



class PackageFirstPage:
  def __init__(self, content):
    self.content = content

  @classmethod
  def create_url(cls):
    return "http://info.jpexpress.jp/confirm/confirmIndex.html"

  @classmethod
  def create_request(cls):
    return urllib2.Request(
      url = cls.create_url())

  @classmethod
  def open(cls):
    request = cls.create_request()
    return urllib2.urlopen(request)

  @classmethod
  def get_content(cls):
    io = cls.open()
    try:
      return io.read()
    finally:
      io.close()

  @classmethod
  def get(cls):
    return cls(cls.get_content())


class PackageFirstPageParser:
  @classmethod
  def parse(cls, src):
    return {
      "jsessionid": cls.get_jsession_id(src),
    }

  @classmethod
  def get_jsession_id(cls, src):
    pattern = re.compile(r"jsessionid=([0-9A-Z]+\.[0-9A-Z]+_[0-9A-Z]+)")
    match   = pattern.search(src)
    return match.group(1) if match is not None else None


class PackageListPage:
  def __init__(self, content):
    self.content = content

  @classmethod
  def create_url(cls, jsession_id):
    return "http://info.jpexpress.jp/confirm/confirmIndex.html;jsessionid=" + jsession_id

  @classmethod
  def create_base_params(cls):
    return {
      "includeChildBody:confirmIndexForm:doConfirmCareerList": "",
      "includeChildBody:confirmIndexForm/confirm/confirmIndex.html": "includeChildBody:confirmIndexForm",
      "includeChildBody:confirmIndexForm:denpyoNo0": "",
      "includeChildBody:confirmIndexForm:denpyoNo1": "",
      "includeChildBody:confirmIndexForm:denpyoNo2": "",
      "includeChildBody:confirmIndexForm:denpyoNo3": "",
      "includeChildBody:confirmIndexForm:denpyoNo4": "",
      "includeChildBody:confirmIndexForm:denpyoNo5": "",
      "includeChildBody:confirmIndexForm:denpyoNo6": "",
      "includeChildBody:confirmIndexForm:denpyoNo7": "",
      "includeChildBody:confirmIndexForm:denpyoNo8": "",
      "includeChildBody:confirmIndexForm:denpyoNo9": "",
    }

  @classmethod
  def create_number_params(cls, numbers):
    params = {}
    for i, number in enumerate(numbers[:10]):
      params["includeChildBody:confirmIndexForm:denpyoNo%i" % i] = number
    return params

  @classmethod
  def create_params(cls, numbers):
    params = cls.create_base_params()
    params.update(cls.create_number_params(numbers))
    return params

  @classmethod
  def create_request(cls, jsession_id, numbers):
    params = cls. create_params(numbers)
    return urllib2.Request(
      url  = cls.create_url(jsession_id),
      data = urllib.urlencode(params))

  @classmethod
  def open(cls, jsession_id, numbers):
    request = cls.create_request(jsession_id, numbers)
    return urllib2.urlopen(request)

  @classmethod
  def get_content(cls, jsession_id, numbers):
    io = cls.open(jsession_id, numbers)
    try:
      return io.read()
    finally:
      io.close()

  @classmethod
  def get(cls, jsession_id, numbers):
    return cls(cls.get_content(jsession_id, numbers))


class PackageListPageParser:
  @classmethod
  def parse(cls, src):
    doc = BeautifulSoup(src)
    list_table = cls.get_list_table(doc)

    return {
      "list": cls.parse_list_table(list_table),
    }

  @classmethod
  def get_list_table(cls, doc):
    return doc.find("div", {"id": "isGetData"}).find("table")

  @classmethod
  def parse_list_table(cls, list_table):
    list_rows = list_table.findAll("tr", recursive = False)

    results = []
    for index, list_row in enumerate(list_rows):
      if index == 0: continue
      results.append(cls.parse_list_row(list_row))

    return results

  @classmethod
  def parse_list_row(cls, list_row):
    cells = list_row.findAll("td", recursive = False)

    result_no_cell         = cells[0]
    tracking_number_cell   = cells[1]
    current_status_cell    = cells[2]
    accept_date_cell       = cells[3]
    arrival_date_cell      = cells[4]
    handling_division_cell = cells[5]
  
    return {
      u"No"                 : result_no_cell.center.span.string,
      u"送り状番号"         : tracking_number_cell.div.a.contents[0].strip(),
      u"送り状番号:リンク先": tracking_number_cell.div.a["href"],
      u"最新状況"           : current_status_cell.span.contents[0].strip(),
      u"最新状況:日時"      : current_status_cell.span.contents[2].strip(),
      u"受付日"             : accept_date_cell.span.contents[0].strip(),
      u"お届け指定日"       : arrival_date_cell.center.span.contents[1].strip(),
      u"扱区分"             : handling_division_cell.center.span.contents[0].strip(),
    }


class PackageDetailPage:
  def __init__(self):
    pass

  @classmethod
  def create_url(cls, jsession_id, params):
    return "http://info.jpexpress.jp/confirm/confirmDetail.html;jsessionid=" + jsession_id + "?" + params
