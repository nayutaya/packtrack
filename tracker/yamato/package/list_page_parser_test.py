# -*- coding: utf-8 -*-

import unittest

from list_page_parser import ListPageParser

class TestListPageParser(unittest.TestCase):
  def setUp(self):
    pass

  def read_fixture(self, filename):
    io = open("fixtures/" + filename, "rb")
    try:
      return io.read()
    finally:
      io.close()

  def test_parser__count01(self):
    target = ListPageParser.parse
    expected = {
      u"一覧": [
        {
          u"伝票番号"      : u"2253-0009-9640",
          u"メッセージ"    : u"このお品物はお届けが済んでおります。お問い合わせはサービスセンターまでお願いいたします。",
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
      target(self.read_fixture("list_count01.html")))

  def test_parser__count02(self):
    target = ListPageParser.parse
    expected = {
      u"一覧": [
        {
          u"伝票番号"      : u"2253-0299-8793",
          u"メッセージ"    : u"このお品物はお届けが済んでおります。お問い合わせはサービスセンターまでお願いいたします。",
          u"商品名"        : u"宅急便",
          u"お届け予定日時": u"06/14　08:00-12:00",
        },
        {
          u"伝票番号"      : u"2253-0316-9976",
          u"メッセージ"    : u"このお品物はお届けが済んでおります。お問い合わせはサービスセンターまでお願いいたします。",
          u"商品名"        : u"宅急便",
          u"お届け予定日時": u"06/17",
        },
      ],
    }
    actual = target(self.read_fixture("list_count02.html"))
    del actual[u"一覧"][0][u"詳細"]
    del actual[u"一覧"][1][u"詳細"]
    self.assertEqual(expected, actual)

  def test_parser__count_all(self):
    target = ListPageParser.parse
    cases = [
      ("list_count01.html", [
          (u"2253-0009-9640", 3)]),
      ("list_count02.html", [
          (u"2253-0299-8793", 4),
          (u"2253-0316-9976", 4)]),
      ("list_count03.html", [
          (u"2253-0341-5632", 7),
          (u"2253-0354-9181", 5),
          (u"2253-0529-2332", 6)]),
      ("list_count04.html", [
          (u"2253-4716-4906", 6),
          (u"2497-0143-1674", 4),
          (u"2497-0224-5564", 2),
          (u"2497-0259-5984", 5)]),
      ("list_count05.html", [
          (u"2497-0318-8405", 3),
          (u"2497-0826-0970", 4),
          (u"2497-0832-2905", 3),
          (u"2497-1190-3571", 4),
          (u"2497-2674-2926", 4)]),
      ("list_count06.html", [
          (u"2497-3352-0540", 4),
          (u"2497-3610-7003", 6),
          (u"2497-3614-0916", 6),
          (u"2497-3951-0790", 5),
          (u"2497-3959-4031", 3),
          (u"2497-3977-4815", 3)]),
      ("list_count07.html", [
          (u"2497-4000-7075", 6),
          (u"2497-4946-3353", 2),
          (u"2497-4962-2780", 2),
          (u"2497-4964-4502", 5),
          (u"2497-6971-1516", 5),
          (u"2497-7027-9150", 5),
          (u"2497-7058-7345", 5)]),
      ("list_count08.html", [
          (u"2497-7265-8634", 4),
          (u"2497-7266-7852", 5),
          (u"2497-9457-6312", 3),
          (u"2497-9480-2143", 3),
          (u"2497-9672-4726", 4),
          (u"2499-6083-6576", 3),
          (u"2253-0009-9640", 3),
          (u"2253-0299-8793", 4)]),
      ("list_count09.html", [
          (u"2253-0316-9976", 4),
          (u"2253-0341-5632", 7),
          (u"2253-0354-9181", 5),
          (u"2253-0529-2332", 6),
          (u"2253-4716-4906", 6),
          (u"2497-0143-1674", 4),
          (u"2497-0224-5564", 2),
          (u"2497-0259-5984", 5),
          (u"2497-0318-8405", 3)]),
      ("list_count10.html", [
          (u"2497-0826-0970", 4),
          (u"2497-0832-2905", 3),
          (u"2497-1190-3571", 4),
          (u"2497-2674-2926", 4),
          (u"2497-3352-0540", 4),
          (u"2497-3610-7003", 6),
          (u"2497-3614-0916", 6),
          (u"2497-3951-0790", 5),
          (u"2497-3959-4031", 3),
          (u"2497-3977-4815", 3)]),
    ]

    for filename, expected in cases:
      page = target(self.read_fixture(filename))
      actual = []
      for record in page[u"一覧"]:
        tracking_number   = record[u"伝票番号"]
        number_of_details = len(record[u"詳細"])
        actual.append((tracking_number, number_of_details))
      self.assertEqual(expected, actual)

  def test_parser__notexist(self):
    target = ListPageParser.parse
    expected = {
      u"一覧": [
        {
          u"伝票番号"      : u"9999-9999-9994",
          u"メッセージ"    : u"お問い合わせいただいた伝票番号は、今現在コンピュータに登録されておりません。最寄りのお客様サービスセンターまでお問い合わせ下さい。",
          u"商品名"        : None,
          u"お届け予定日時": None,
          u"詳細"          : None,
        },
      ],
    }
    self.assertEqual(
      expected,
      target(self.read_fixture("list_notexist.html")))

  def test_parser__transfer(self):
    target = ListPageParser.parse
    expected = {
      u"一覧": [
        {
          u"伝票番号"      : u"2497-2497-3934",
          u"メッセージ"    : None,
          u"商品名"        : u"宅急便",
          u"お届け予定日時": u"09/03",
          u"詳細"          : [
            {
              u"荷物状況"    : u"発送",
              u"日付"        : u"09/01",
              u"時刻"        : u"18:21",
              u"担当店名"    : u"緑八朔センター",
              u"担当店コード": u"028682",
            },
            {
              u"荷物状況"    : u"作業店通過",
              u"日付"        : u"09/01",
              u"時刻"        : u"20:56",
              u"担当店名"    : u"神奈川ベース店",
              u"担当店コード": u"028990",
            },
          ],
        },
      ],
    }
    actual = target(self.read_fixture("list_transfer.html"))
    self.assertEqual(expected, actual)

  def test_parser__misc01(self):
    target = ListPageParser.parse
    actual = target(self.read_fixture("list_misc01.html"))

  def test_parser__misc02(self):
    target = ListPageParser.parse
    actual = target(self.read_fixture("list_misc02.html"))

  def test_parser__misc03(self):
    target = ListPageParser.parse
    actual = target(self.read_fixture("list_misc03.html"))

  def test_parser__misc04(self):
    target = ListPageParser.parse
    actual = target(self.read_fixture("list_misc04.html"))

if __name__ == "__main__":
  unittest.main()
