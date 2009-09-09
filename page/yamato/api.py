# -*- coding: utf-8 -*-

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
