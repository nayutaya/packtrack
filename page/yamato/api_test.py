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
          u"メッセージ"    : u"a",
          u"商品名"        : u"b",
          u"お届け予定日時": u"c",
          u"詳細"          : [
            {
              u"荷物状況"    : u"d1",
              u"日付"        : u"09/01",
              u"時刻"        : u"18:21",
              u"担当店名"    : u"d2",
              u"担当店コード": u"d3",
            },
            {
              u"荷物状況"    : u"e1",
              u"日付"        : u"09/01",
              u"時刻"        : u"20:56",
              u"担当店名"    : u"e2",
              u"担当店コード": u"e3",
            },
          ],
        }
      ],
    }
    expected = {
      u"249724973934": {
        u"message": u"a",
        u"type"   : u"b",
        u"detail" : {
          u"delivery_time": u"c",
        },
        u"history": [
          {
            u"state"       : u"d1",
            u"time"        : u"2009-09-01 18:21",
            u"station_name": u"d2",
            u"station_code": u"d3",
          },
          {
            u"state"       : u"e1",
            u"time"        : u"2009-09-01 20:56",
            u"station_name": u"e2",
            u"station_code": u"e3",
          },
        ],
      },
    }
    self.assertEqual(expected, target(info))

if __name__ == "__main__":
  unittest.main()
