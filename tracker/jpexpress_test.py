# -*- coding: utf-8 -*-

import unittest

import jpexpress


class TestPackageTrackingNumber(unittest.TestCase):
  def setUp(self):
    pass

  def test_create_check_digit(self):
    target = jpexpress.PackageTrackingNumber.create_check_digit
    self.assertEqual("0", target("00000000000"))
    self.assertEqual("6", target("00000000006"))
    self.assertEqual("0", target("00000000007"))
    self.assertEqual("4", target("99999999999"))

  def test_split_check_digit(self):
    target = jpexpress.PackageTrackingNumber.split_check_digit
    self.assertEqual(("00000000000", "0"), target("000000000000"))
    self.assertEqual(("01234567890", "1"), target("012345678901"))

  def test_is_valid(self):
    target = jpexpress.PackageTrackingNumber.is_valid
    self.assertEqual(True, target("000000000000"))
    self.assertEqual(True, target("012345678903"))
    self.assertEqual(True, target("999999999994"))

    self.assertEqual(False, target("00000000000"))
    self.assertEqual(False, target("0000000000000"))
    self.assertEqual(False, target("aaaaaaaaaaaa"))
    self.assertEqual(False, target("000000000001"))

# TODO: PackageTrackingSessionクラスのテストを記述

# TODO: PackageFirstPageクラスのテストを記述

class TestPackageFirstPageParser(unittest.TestCase):
  def setUp(self):
    pass

  def test_parse(self):
    target = jpexpress.PackageFirstPageParser.parse

    src = open("test/jpexpress/first.html", "rb").read()
    expected = {
      "jsessionid": "39A6C0TBKUFKR11NTUM7N3FKKDGU03V05N0I3F5FMQMFFB9I23PKAAF9B4HG2000JO000000.WU001_001",
    }
    self.assertEqual(expected, target(src))


# TODO: PackageListPageクラスのテストを記述

class TestPackageListPageParser(unittest.TestCase):
  def setUp(self):
    pass

  def read_data(self, filename):
    io = open("test/jpexpress/" + filename, "rb")
    try:
      return io.read()
    finally:
      io.close()

  def test_parse__notexist(self):
    expected = {
      "list": [
        {
          u"No"                 : u"1",
          u"送り状番号"         : u"指定された伝票番号(348089408741)は存在しません。",
          u"送り状番号:リンク先": None,
          u"最新状況"           : None,
          u"最新状況:日時"      : None,
          u"受付日"             : u"該当データ無し",
          u"お届け指定日"       : None,
          u"扱区分"             : None,
        },
      ],
    }
    actual = jpexpress.PackageListPageParser.parse(self.read_data("list_notexist.html"))
    self.assertEqual(expected, actual)

  def test_parse__all_count(self):
    list = [
      ("list_count01.html", [u"1"]),
      ("list_count02.html", [u"1", u"2"]),
      ("list_count03.html", [u"1", u"2", u"3"]),
      ("list_count04.html", [u"1", u"2", u"3", u"4"]),
      ("list_count05.html", [u"1", u"2", u"3", u"4", u"5"]),
      ("list_count06.html", [u"1", u"2", u"3", u"4", u"5", u"6"]),
      ("list_count07.html", [u"1", u"2", u"3", u"4", u"5", u"6", u"7"]),
      ("list_count08.html", [u"1", u"2", u"3", u"4", u"5", u"6", u"7", u"8"]),
      ("list_count09.html", [u"1", u"2", u"3", u"4", u"5", u"6", u"7", u"8", u"9"]),
      ("list_count10.html", [u"1", u"2", u"3", u"4", u"5", u"6", u"7", u"8", u"9", u"10"]),
    ]
    for filename, expected in list:
      src  = self.read_data(filename)
      info = jpexpress.PackageListPageParser.parse(src)
      actual = [record["No"] for record in info["list"]]
      self.assertEqual(expected, actual)

  def test_parse__count01(self):
    expected = {
      "list": [
        {
          u"No"                 : u"1",
          u"送り状番号"         : u"348-01-037-7713",
          u"送り状番号:リンク先": u"confirmDetail.html;jsessionid=FSKBT51D2D6E9P5CT977DDUGFTGU03V05N0I3F47P78NA8SIMJ0KBVGOB8HG2000MC000000.WU001_001?denpyoNo=348-01-037-7713&detailQuery=pspaksba000_000.jsp%3Fuji.verb%3Dstartup%26uji.bean%3Dnittsu.kzd.pspakzdj002_501%26stbInvoiceNo%3D348010377713%26stbDupulicationCheckNo%3D0%26stbInvoiceDSI%3D035%26stbMonthDSI%3D06%26st",
          u"最新状況"           : u"受取が完了いたしました。",
          u"最新状況:日時"      : u"6/25 12:54",
          u"受付日"             : u"6/20",
          u"お届け指定日"       : u"時間指定なし",
          u"扱区分"             : u"ペリカン便",
        },
      ],
    }
    actual = jpexpress.PackageListPageParser.parse(self.read_data("list_count01.html"))
    self.assertEqual(expected, actual)

  def test_parse__count02(self):
    expected = {
      "list": [
        {
          u"No"                 : u"1",
          u"送り状番号"         : u"348-01-077-8570",
          u"送り状番号:リンク先": u"confirmDetail.html;jsessionid=T2GFFDDFNTBF6VF4PGF2UBEOA5GU03V05N0I3F47P78NA8SIMJ0IPCOPB8HG2000NK000000.WU001_001?denpyoNo=348-01-077-8570&detailQuery=pspaksba000_000.jsp%3Fuji.verb%3Dstartup%26uji.bean%3Dnittsu.kzd.pspakzdj002_501%26stbInvoiceNo%3D348010778570%26stbDupulicationCheckNo%3D0%26stbInvoiceDSI%3D028%26stbMonthDSI%3D06%26st",
          u"最新状況"           : u"受取が完了いたしました。",
          u"最新状況:日時"      : u"7/2 18:53",
          u"受付日"             : u"6/30",
          u"お届け指定日"       : u"時間指定なし",
          u"扱区分"             : u"ペリカン便",
        },
        {
          u"No"                 : u"2",
          u"送り状番号"         : u"348-01-087-4444",
          u"送り状番号:リンク先": u"confirmDetail.html;jsessionid=T2GFFDDFNTBF6VF4PGF2UBEOA5GU03V05N0I3F47P78NA8SIMJ0IPCOPB8HG2000NK000000.WU001_001?denpyoNo=348-01-087-4444&detailQuery=pspaksba000_000.jsp%3Fuji.verb%3Dstartup%26uji.bean%3Dnittsu.kzd.pspakzdj002_501%26stbInvoiceNo%3D348010874444%26stbDupulicationCheckNo%3D0%26stbInvoiceDSI%3D022%26stbMonthDSI%3D07%26st",
          u"最新状況"           : u"受取が完了いたしました。",
          u"最新状況:日時"      : u"7/3 19:55",
          u"受付日"             : u"7/ 2",
          u"お届け指定日"       : u"時間指定なし",
          u"扱区分"             : u"ペリカン便",
        },
      ],
    }
    actual = jpexpress.PackageListPageParser.parse(self.read_data("list_count02.html"))
    self.assertEqual(expected, actual)

  def test_parse__accepted(self):
    expected = {
      "list": [
        {
          u"No"                 : u"1",
          u"送り状番号"         : u"348-01-225-3676",
          u"送り状番号:リンク先": u"confirmDetail.html;jsessionid=8HDS3U7DKEVI3KOKP4BLEO1A69GU03V05N0I3F5FMQMFFB9I23PITSBKBSHG2000N4000000.WU001_001?denpyoNo=348-01-225-3676&detailQuery=pspaksba000_000.jsp%3Fuji.verb%3Dstartup%26uji.bean%3Dnittsu.kzd.pspakzdj002_501%26stbInvoiceNo%3D348012253676%26stbDupulicationCheckNo%3D0%26stbInvoiceDSI%3D033%26stbMonthDSI%3D08%26st",
          u"最新状況"           : u"受取が完了いたしました。",
          u"最新状況:日時"      : u"8/10 19:41",
          u"受付日"             : u"8/ 6",
          u"お届け指定日"       : u"時間指定なし",
          u"扱区分"             : u"ペリカン便",
        },
      ],
    }
    actual = jpexpress.PackageListPageParser.parse(self.read_data("list_accepted.html"))
    self.assertEqual(expected, actual)

  def test_parse__arrival(self):
    expected = {
      "list": [
        {
          u"No"                 : u"1",
          u"送り状番号"         : u"348-00-190-9286",
          u"送り状番号:リンク先": u"confirmDetail.html;jsessionid=7L1V11KGCDJ1EP66J7FGLJDPSDGU03V05N0I3F5FE7OC3TA6590BB13MBSHG20000K000000.WU001_003?denpyoNo=348-00-190-9286&detailQuery=pspaksba000_000.jsp%3Fuji.verb%3Dstartup%26uji.bean%3Dnittsu.kzd.pspakzdj002_501%26stbInvoiceNo%3D348001909286%26stbDupulicationCheckNo%3D0%26stbInvoiceDSI%3D014%26stbMonthDSI%3D08%26st",
          u"最新状況"           : u"コンビニ配送センターに到着いたしました。08月27日の１８時以降にご指定の店舗でお受け取りできます。",
          u"最新状況:日時"      : u"8/27",
          u"受付日"             : u"8/26",
          u"お届け指定日"       : u"時間指定なし",
          u"扱区分"             : u"ペリカン便",
        },
      ],
    }
    actual = jpexpress.PackageListPageParser.parse(self.read_data("list_arrival.html"))
    self.assertEqual(expected, actual)

  def test_parse__delivery(self):
    expected = {
      "list": [
        {
          u"No"                 : u"1",
          u"送り状番号"         : u"380-73-835-2890",
          u"送り状番号:リンク先": u"confirmDetail.html;jsessionid=GH12IVIGT6J0QL1HJAANM7TFHDGU03V05N0I3F1LQ5DPNRJ84ISJDIJRBSHG20003O000000.WU001_004?denpyoNo=380-73-835-2890&detailQuery=pspaksba000_000.jsp%3Fuji.verb%3Dstartup%26uji.bean%3Dnittsu.kzd.pspakzdj002_501%26stbInvoiceNo%3D380738352890%26stbDupulicationCheckNo%3D0%26stbInvoiceDSI%3D044%26stbMonthDSI%3D07%26st",
          u"最新状況"           : u"配達完了いたしました。",
          u"最新状況:日時"      : u"7/6 8:57",
          u"受付日"             : u"7/ 4",
          u"お届け指定日"       : None,
          u"扱区分"             : u"ペリカン便",
        },
      ],
    }
    actual = jpexpress.PackageListPageParser.parse(self.read_data("list_delivery.html"))
    self.assertEqual(expected, actual)

  def test_parse__inquiry(self):
    expected = {
      "list": [
        {
          u"No"                 : u"1",
          u"送り状番号"         : u"348-00-178-6042",
          u"送り状番号:リンク先": u"confirmDetail.html;jsessionid=EE1J77NDEDH904G2B5QIN4QJJLGU03V05N0I3F1EUKH4D3RP0DAOU73NBSHG2000TC000000.WU001_003?denpyoNo=348-00-178-6042&detailQuery=pspaksba000_000.jsp%3Fuji.verb%3Dstartup%26uji.bean%3Dnittsu.kzd.pspakzdj002_501%26stbInvoiceNo%3D348001786042%26stbDupulicationCheckNo%3D0%26stbInvoiceDSI%3D002%26stbMonthDSI%3D07%26st",
          u"最新状況"           : u"弊社お問い合わせ窓口店にお問合わせ下さい。",
          u"最新状況:日時"      : u"7/21",
          u"受付日"             : u"7/10",
          u"お届け指定日"       : u"時間指定なし",
          u"扱区分"             : u"ペリカン便",
        },
      ],
    }
    actual = jpexpress.PackageListPageParser.parse(self.read_data("list_inquiry.html"))
    self.assertEqual(expected, actual)


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
      #u"最新状況"    : u"受取が完了いたしました。",
      #u"受付日"      : u"2009/ 8/ 6",
      #u"お届け指定日": u"時間指定なし",
      #u"扱区分"      : u"ペリカン便",
      #u"商品情報"    : u"コンビニ受取",
      #u"個数"        : u"1",
      #u"重量／サイズ": u"６０サイズ",
    }
    actual = jpexpress.PackageDetailPageParser.parse(self.read_data("detail_accepted.html"))
    self.assertEqual(expected, actual)

  def test_parse__arrival(self):
    expected = {
      u"送り状番号"  : None,
      u"最新状況"    : None,
      u"受付日"      : None,
      u"お届け指定日": None,
      u"扱区分"      : None,
      u"商品情報"    : None,
      u"個数"        : None,
      u"重量／サイズ": None,
    }
    #actual = jpexpress.PackageDetailPageParser.parse(self.read_data("detail_arrival.html"))
    #self.assertEqual(expected, actual)

  def test_parse__delivery(self):
    expected = {
      u"送り状番号"  : None,
      u"最新状況"    : None,
      u"受付日"      : None,
      u"お届け指定日": None,
      u"扱区分"      : None,
      u"商品情報"    : None,
      u"個数"        : None,
      u"重量／サイズ": None,
    }
    #actual = jpexpress.PackageDetailPageParser.parse(self.read_data("detail_delivery.html"))
    #self.assertEqual(expected, actual)

  def test_parse__inquiry(self):
    expected = {
      u"送り状番号"  : None,
      u"最新状況"    : None,
      u"受付日"      : None,
      u"お届け指定日": None,
      u"扱区分"      : None,
      u"商品情報"    : None,
      u"個数"        : None,
      u"重量／サイズ": None,
    }
    #actual = jpexpress.PackageDetailPageParser.parse(self.read_data("detail_inquiry.html"))
    #self.assertEqual(expected, actual)


if __name__ == "__main__":
  unittest.main()
