# -*- coding: utf-8 -*-

class ListParameter:
  def __init__(self, params):
    self.numbers = self.parse_numbers(params.get("numbers"))

  @classmethod
  def parse_numbers(cls, numbers):
    results = []
    if numbers is not None:
      for number in numbers.split(","):
        if number != "":
          results.append(number)
    return results
