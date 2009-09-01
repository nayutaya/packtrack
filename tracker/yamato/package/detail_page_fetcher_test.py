# -*- coding: utf-8 -*-

import unittest

from detail_page_fetcher import DetailPageFetcher

class TestDetailPageFetcher(unittest.TestCase):
  def setUp(self):
    pass

  def test_create_url(self):
    target = DetailPageFetcher.create_url
    self.assertEqual(
      "http://toi.kuronekoyamato.co.jp/cgi-bin/tneko",
      target())

  def test_create_base_params(self):
    target = DetailPageFetcher.create_base_params

    expected = [
      "number00",
      "number01",
      "number02",
      "number03",
      "number04",
      "number05",
      "number06",
      "number07",
      "number08",
      "number09",
      "number10",
      "timeid",
    ]
    expected.sort()
    actual = target().keys()
    actual.sort()
    self.assertEqual(expected, actual)

    for key, value in target().items():
      if key == "number00":
        self.assertEqual("1", value)
      else:
        self.assertEqual("", value)

  def test_create_number_params__empty(self):
    target = DetailPageFetcher.create_number_params
    self.assertEqual({}, target([]))

  def test_create_number_params__1(self):
    target = DetailPageFetcher.create_number_params
    expected = {
      "number01": "1",
    }
    self.assertEqual(expected, target(["1"]))

  def test_create_number_params__10(self):
    target = DetailPageFetcher.create_number_params
    expected = {
      "number01": "1",
      "number02": "2",
      "number03": "3",
      "number04": "4",
      "number05": "5",
      "number06": "6",
      "number07": "7",
      "number08": "8",
      "number09": "9",
      "number10": "10",
    }
    self.assertEqual(expected, target(["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]))

  def test_create_number_params__11(self):
    target = DetailPageFetcher.create_number_params
    proc = lambda: target(["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"])
    self.assertRaises(ValueError, proc)

if __name__ == "__main__":
  unittest.main()
