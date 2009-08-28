# -*- coding: utf-8 -*-

import unittest

import jpexpress


class TestPackageTrackingNumber(unittest.TestCase):
  def setUp(self):
    pass

  def test_create_check_digit(self):
    target = jpexpress.PackageTrackingNumber.create_check_digit
    self.assertEqual("0", target("00000000000"))
    self.assertEqual("1", target("00000000001"))
    self.assertEqual("6", target("00000000006"))
    self.assertEqual("0", target("00000000007"))
    self.assertEqual("4", target("99999999999"))


if __name__ == "__main__":
  unittest.main()
