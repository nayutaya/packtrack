# -*- coding: utf-8 -*-

import unittest

from tracking_number import TrackingNumber

class TestTrackingNumber(unittest.TestCase):
  def setUp(self):
    pass

  def test_create_check_digit(self):
    target = TrackingNumber.create_check_digit
    self.assertEqual("0", target("00000000000"))
    self.assertEqual("6", target("00000000006"))
    self.assertEqual("0", target("00000000007"))
    self.assertEqual("4", target("99999999999"))

  def test_split_check_digit(self):
    target = TrackingNumber.split_check_digit
    self.assertEqual(("00000000000", "0"), target("000000000000"))
    self.assertEqual(("01234567890", "1"), target("012345678901"))

  def test_is_valid(self):
    target = TrackingNumber.is_valid
    self.assertEqual(True, target("000000000000"))
    self.assertEqual(True, target("012345678903"))
    self.assertEqual(True, target("999999999994"))

    self.assertEqual(False, target("00000000000"))
    self.assertEqual(False, target("0000000000000"))
    self.assertEqual(False, target("aaaaaaaaaaaa"))
    self.assertEqual(False, target("000000000001"))

  def test_create_random_number(self):
    target = TrackingNumber.create_random_number
    self.assertEqual(False, (target() == target()))
    self.assertEqual(True, TrackingNumber.is_valid(target()))
    self.assertEqual("0",  target("0")[:1])
    self.assertEqual("12", target("12")[:2])

if __name__ == "__main__":
  unittest.main()
