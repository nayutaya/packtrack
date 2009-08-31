# -*- coding: utf-8 -*-

import unittest

import jpexpress



# TODO: PackageDetailPageクラスのテストを記述

class TestPackageDetailPageParser(unittest.TestCase):
  def setUp(self):
    pass

  def read_data(self, filename):
    io = open("test/jpexpress/" + filename, "rb")
    try:
      return io.read()
    finally:
      io.close()

  def test_parse__accepted(self):
    expected = {
      u"送り状番号"  : u"348-01-225-3676",
      u"最新状況"    : u"受取が完了いたしました。",
      u"受付日"      : u"2009/ 8/ 6",
      u"お届け指定日": u"時間指定なし",
      u"扱区分"      : u"ペリカン便",
      u"商品情報"    : u"コンビニ受取",
      u"個数"        : u"1",
      u"重量／サイズ": u"６０サイズ",
    }
    actual = jpexpress.PackageDetailPageParser.parse(self.read_data("detail_accepted.html"))
    self.assertEqual(expected, actual)

  def test_parse__arrival(self):
    expected = {
      u"送り状番号"  : u"348-01-298-4885",
      u"最新状況"    : u"コンビニ配送センターに到着いたしました。作業日時の１８時以降にご指定の店舗でお受け取りできます。",
      u"受付日"      : u"2009/ 8/26",
      u"お届け指定日": u"時間指定なし",
      u"扱区分"      : u"ペリカン便",
      u"商品情報"    : u"コンビニ受取",
      u"個数"        : u"1",
      u"重量／サイズ": u"６０サイズ",
    }
    actual = jpexpress.PackageDetailPageParser.parse(self.read_data("detail_arrival.html"))
    self.assertEqual(expected, actual)

  def test_parse__delivery(self):
    expected = {
      u"送り状番号"  : u"380-73-835-2890",
      u"最新状況"    : u"配達完了いたしました。",
      u"受付日"      : u"2009/ 7/ 4　15:56",
      u"お届け指定日": u"&nbsp;",
      u"扱区分"      : u"ペリカン便",
      u"商品情報"    : u"一般ペリカン",
      u"個数"        : u"1",
      u"重量／サイズ": u"８０サイズ",
    }
    actual = jpexpress.PackageDetailPageParser.parse(self.read_data("detail_delivery.html"))
    self.assertEqual(expected, actual)

  def test_parse__inquiry(self):
    expected = {
      u"送り状番号"  : u"348-00-178-6042",
      u"最新状況"    : u"弊社お問い合わせ窓口店にお問合わせ下さい。",
      u"受付日"      : u"2009/ 7/10",
      u"お届け指定日": u"時間指定なし",
      u"扱区分"      : u"ペリカン便",
      u"商品情報"    : u"コンビニ受取",
      u"個数"        : u"1",
      u"重量／サイズ": u"６０サイズ",
    }
    actual = jpexpress.PackageDetailPageParser.parse(self.read_data("detail_inquiry.html"))
    self.assertEqual(expected, actual)


if __name__ == "__main__":
  unittest.main()
