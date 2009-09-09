# -*- coding: utf-8 -*-

import unittest

from api import ListParameter
from api import ListConverter

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

  def test_parse_include_detail(self):
    target = ListParameter.parse_include_detail

    self.assertEqual(False, target(None))
    self.assertEqual(False, target("false"))

    self.assertEqual(True, target("true"))

  def test_parse_include_history(self):
    target = ListParameter.parse_include_history

    self.assertEqual(False, target(None))
    self.assertEqual(False, target("false"))

    self.assertEqual(True, target("true"))

  def test_init__empty(self):
    target = ListParameter

    obj = target({})
    self.assertEqual([],    obj.numbers)
    self.assertEqual(False, obj.include_detail)
    self.assertEqual(False, obj.include_history)

  def test_init__full(self):
    target = ListParameter

    obj = target({
      "numbers"        : "1,2,3",
      "include_detail" : "true",
      "include_history": "true",
    })
    self.assertEqual(["1", "2", "3"], obj.numbers)
    self.assertEqual(True, obj.include_detail)
    self.assertEqual(True, obj.include_history)

class TestListConverter(unittest.TestCase):
  def setUp(self):
    pass

  def test_convert__empty(self):
    target = ListConverter.convert

    self.assertEqual({}, target({}))

  def test_convert__full(self):
    target = ListConverter.convert

    info = {
      u"一覧": [
        {
          u"伝票番号"      : u"2497-2497-3934",
          #u"メッセージ"    : u"a",
        }
      ],
    }

    expected = {
      u"249724973934": {
        u"message": None,
      },
    }

    self.assertEqual(expected, target(info))

if __name__ == "__main__":
  unittest.main()
