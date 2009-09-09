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

      result[tracking_number] = {
        u"message": None,
      }


    return result
