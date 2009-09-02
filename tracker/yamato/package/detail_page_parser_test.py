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
      "list": [
        {
          u"伝票番号": u"2253-0009-9640",
          u"メッセージ": u"このお品物はお届けが済んでおります。\nお問い合わせはサービスセンターまでお願いいたします。",
        },
      ],
    }
    self.assertEqual(
      expected,
      target(self.read_fixture("detail_count01.html")))

if __name__ == "__main__":
  unittest.main()
