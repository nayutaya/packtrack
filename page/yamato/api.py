# -*- coding: utf-8 -*-

class ListParameter:
  def __init__(self, params):
    self.numbers        = self.parse_numbers(params.get("numbers"))
    self.include_detail = self.parse_include_detail(params.get("include_detail"))

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
