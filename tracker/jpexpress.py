# -*- coding: utf-8 -*-

import re
import urllib
import urllib2
from BeautifulSoup import BeautifulSoup


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
