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

# TODO: PackageDetailPageクラスのテストを記述


if __name__ == "__main__":
  unittest.main()
