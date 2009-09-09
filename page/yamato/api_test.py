# -*- coding: utf-8 -*-

import unittest

from api import ListParameter

class TestListParameter(unittest.TestCase):
  def setUp(self):
    pass

  def test_parse_numbers(self):
    target = ListParameter.parse_numbers

    self.assertEqual([], target(None))
    self.assertEqual([], target(""))

    self.assertEqual(["1"], target("1"))
    self.assertEqual(["1"], target("1,"))
    self.assertEqual(["1", "2"], target("1,2"))
    self.assertEqual(["1", "2"], target("1,2,"))

  def test_init__empty(self):
    target = ListParameter

    obj = target({})
    self.assertEqual([], obj.numbers)

  def test_init__full(self):
    target = ListParameter

    obj = target({"numbers": "1,2,3"})
    self.assertEqual(["1", "2", "3"], obj.numbers)

if __name__ == "__main__":
  unittest.main()
