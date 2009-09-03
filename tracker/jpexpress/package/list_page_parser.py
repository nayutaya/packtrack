# -*- coding: utf-8 -*-

import re
from BeautifulSoup import BeautifulSoup

# 一覧ページ解析クラス
class ListPageParser:
  @classmethod
  def parse(cls, src):
    doc = BeautifulSoup(src)
    list_table = cls.get_list_table(doc)

    return {
      u"一覧": cls.parse_list_table(list_table),
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
      arrival_date = "".join(arrival_date_cell.center.span.findAll(text = True))

    handling_division = None
    if handling_division_cell.center.span.contents[0].strip is not None:
      handling_division = handling_division_cell.center.span.contents[0].strip()

    tracking_number_params = None
    if tracking_number_href is not None:
      pattern = re.compile(r"\?(.*)$")
      match   = pattern.search(tracking_number_href)
      if match is not None:
        tracking_number_params = match.group(1)

    return {
      u"No"                   : result_no_cell.center.span.string,
      u"送り状番号"           : tracking_number,
      u"送り状番号:リンク先"  : tracking_number_href,
      u"送り状番号:パラメータ": tracking_number_params,
      u"最新状況"             : current_status,
      u"最新状況:日時"        : current_status_time,
      u"受付日"               : accept_date_cell.span.contents[0].strip(),
      u"お届け指定日"         : arrival_date,
      u"扱区分"               : handling_division,
    }
