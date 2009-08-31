# -*- coding: utf-8 -*-

import re
import urllib
import urllib2
from BeautifulSoup import BeautifulSoup


# 先頭ページクラス
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

# 先頭ページ解析クラス
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

# 一覧ページクラス
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

# 一覧ページ解析クラス
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

    tracking_number      = None
    tracking_number_href = None
    if tracking_number_cell.div is not None:
      if tracking_number_cell.div.a is not None:
        tracking_number      = tracking_number_cell.div.a.contents[0].strip()
        tracking_number_href = tracking_number_cell.div.a["href"]
      else:
        tracking_number      = tracking_number_cell.div.contents[0].strip()
        tracking_number_href = None

    current_status = current_status_cell.span.contents[0].strip()
    if current_status == u"&nbsp;&nbsp;":
      current_status = None

    current_status_time = current_status_cell.span.contents[2].strip()
    if current_status_time == "":
      current_status_time = None

    arrival_date = None
    if len(arrival_date_cell.center.span.contents) >= 2:
      arrival_date = arrival_date_cell.center.span.contents[1].strip()

    handling_division = None
    if handling_division_cell.center.span.contents[0].strip is not None:
      handling_division = handling_division_cell.center.span.contents[0].strip()

    return {
      u"No"                 : result_no_cell.center.span.string,
      u"送り状番号"         : tracking_number,
      u"送り状番号:リンク先": tracking_number_href,
      u"最新状況"           : current_status,
      u"最新状況:日時"      : current_status_time,
      u"受付日"             : accept_date_cell.span.contents[0].strip(),
      u"お届け指定日"       : arrival_date,
      u"扱区分"             : handling_division,
    }

# 詳細ページクラス
class PackageDetailPage:
  def __init__(self):
    pass

  @classmethod
  def create_url(cls, jsession_id, params):
    return "http://info.jpexpress.jp/confirm/confirmDetail.html;jsessionid=" + jsession_id + "?" + params

# 詳細ページ解析クラス
class PackageDetailPageParser:
  @classmethod
  def parse(cls, src):
    doc = BeautifulSoup(src)
    detail_table = cls.get_detail_table(doc)
    return cls.parse_detail_table(detail_table)

  @classmethod
  def get_detail_table(cls, doc):
    return doc.find("div", {"id": "isGetData"}).find("table")

  @classmethod
  def parse_detail_table(cls, detail_table):
    rows = detail_table.findAll("tr", recursive = False)

    cells1 = rows[2].findAll("td", recursive = False)
    cells2 = rows[3].findAll("td", recursive = False)

    tracking_number_cell   = cells1[0]
    current_status_cell    = cells1[1]
    accept_date_cell       = cells1[2]
    arrival_date_cell      = cells1[3]
    handling_division_cell = cells2[0]
    information_cell       = cells2[1]
    quantity_cell          = cells2[2]
    dimension_cell         = cells2[3]

    return {
      u"送り状番号"  : tracking_number_cell.center.span.contents[0].strip(),
      u"最新状況"    : current_status_cell.center.span.contents[0].strip(),
      u"受付日"      : accept_date_cell.center.span.contents[0].strip(),
      u"お届け指定日": arrival_date_cell.center.span.contents[0].strip(),
      u"扱区分"      : handling_division_cell.center.span.contents[0].strip(),
      u"商品情報"    : information_cell.center.span.contents[0].strip(),
      u"個数"        : quantity_cell.center.span.contents[0].strip(),
      u"重量／サイズ": dimension_cell.center.span.contents[0].strip(),
    }
