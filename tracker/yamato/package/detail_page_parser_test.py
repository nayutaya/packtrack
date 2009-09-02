# -*- coding: utf-8 -*-

import unittest

from detail_page_parser import DetailPageParser

class TestDetailPageParser(unittest.TestCase):
  def setUp(self):
    pass

  def read_fixture(self, filename):
    io = open("fixtures/" + filename, "rb")
    try:
      return io.read()
    finally:
      io.close()

  def test_parser__count01(self):
    target = DetailPageParser.parse

    expected = {
      "一覧": [
        {
          u"伝票番号"      : u"2253-0009-9640",
          u"メッセージ"    : u"このお品物はお届けが済んでおります。\nお問い合わせはサービスセンターまでお願いいたします。",
          u"商品名"        : u"宅急便",
          u"お届け予定日時": u"07/17　08:00-12:00",
          u"詳細"          : [
            {
              u"荷物状況"    : u"荷物受付",
              u"日付"        : u"07/15",
              u"時刻"        : u"17:08",
              u"担当店名"    : u"北九州物流システム支店",
              u"担当店コード": u"091770",
            },
            {
              u"荷物状況"    : u"発送",
              u"日付"        : u"07/15",
              u"時刻"        : u"17:08",
              u"担当店名"    : u"北九州物流システム支店",
              u"担当店コード": u"091770",
            },
            {
              u"荷物状況"    : u"配達完了",
              u"日付"        : u"07/17",
              u"時刻"        : u"11:55",
              u"担当店名"    : u"宮城利府センター",
              u"担当店コード": u"013253",
            },
          ],
        },
      ],
    }
    self.assertEqual(
      expected,
      target(self.read_fixture("detail_count01.html")))

  def test_parser__count02(self):
    target = DetailPageParser.parse

    expected = {
      "一覧": [
        {
          u"伝票番号"      : u"2253-0299-8793",
          u"メッセージ"    : u"このお品物はお届けが済んでおります。\nお問い合わせはサービスセンターまでお願いいたします。",
          u"商品名"        : u"宅急便",
          u"お届け予定日時": u"06/14　08:00-12:00",
        },
        {
          u"伝票番号"      : u"2253-0316-9976",
          u"メッセージ"    : u"このお品物はお届けが済んでおります。\nお問い合わせはサービスセンターまでお願いいたします。",
          u"商品名"        : u"宅急便",
          u"お届け予定日時": u"06/17",
        },
      ],
    }
    actual = target(self.read_fixture("detail_count02.html"))
    del actual["一覧"][0][u"詳細"]
    del actual["一覧"][1][u"詳細"]
    self.assertEqual(expected, actual)


  def test_parser__count_all(self):
    target = DetailPageParser.parse

    cases = [
      ("detail_count02.html", [
          (u"2253-0299-8793", 4),
          (u"2253-0316-9976", 4)]),
    ]

    for filename, expected in cases:
      info = target(self.read_fixture(filename))
      actual = []
      for record in info["一覧"]:
        tracking_number   = record[u"伝票番号"]
        number_of_details = len(record[u"詳細"])
        actual.append((tracking_number, number_of_details))
      self.assertEqual(expected, actual)

if __name__ == "__main__":
  unittest.main()
