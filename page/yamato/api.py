# -*- coding: utf-8 -*-

import re

# 一覧API パラメータクラス
class ListParameter:
  def __init__(self, params):
    self.numbers         = self.parse_numbers(params.get("numbers"))
    self.include_detail  = self.parse_include_detail(params.get("include_detail"))
    self.include_history = self.parse_include_history(params.get("include_history"))

  @classmethod
  def parse_numbers(cls, numbers):
    results = []
    if numbers is not None:
      for number in numbers.split(","):
        if number != "":
          results.append(number)
    return results

  @classmethod
  def parse_include_detail(cls, include_detail):
    return (include_detail == "true")

  @classmethod
  def parse_include_history(cls, include_history):
    return (include_history == "true")

# 一覧API コンバータクラス
class ListConverter:
  @classmethod
  def convert(cls, info):
    records = info.get(u"一覧")
    if records is None:
      return {}

    result = {}
    for record in records:
      tracking_number = re.sub("-", "", record[u"伝票番号"])

      detail = {
        u"delivery_time": record[u"お届け予定日時"],
      }

      history = []
      detail_records = record[u"詳細"]
      for detail_record in detail_records:
        time  = "2009-"
        time += re.sub("/", "-", detail_record[u"日付"]) # FIXME:
        time += " " + detail_record[u"時刻"]
        his = {
          "state"       : detail_record[u"荷物状況"],
          "time"        : time,
          "station_name": detail_record[u"担当店名"],
          "station_code": detail_record[u"担当店コード"],
        }
        history.append(his)

      result[tracking_number] = {
        u"message": record[u"メッセージ"],
        u"type"   : record[u"商品名"],
        u"detail" : detail,
        u"history": history,
      }

    return result
