# -*- coding: utf-8 -*-

import unittest
import cgi

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

  def test_create_params__empty(self):
    target = DetailPageFetcher.create_params
    expected = DetailPageFetcher.create_base_params()
    self.assertEqual(expected, target([]))

  def test_create_params__empty(self):
    target = DetailPageFetcher.create_params
    expected = DetailPageFetcher.create_base_params()
    expected["number01"] = "1"
    self.assertEqual(expected, target(["1"]))

  def test_create_request(self):
    target = DetailPageFetcher.create_request
    numbers = ["1", "2"]
    request = target(numbers)

    self.assertEqual(
      DetailPageFetcher.create_url(),
      request.get_full_url())

    expected = {}
    for key, value in DetailPageFetcher.create_params(numbers).items():
      if value != "": expected[key] = value
    actual = {}
    for key, value in cgi.parse_qs(request.get_data()).items():
      actual[key] = value[0]
    self.assertEqual(expected, actual)

  def test_open(self):
    target = DetailPageFetcher.open
    io = target(["000000000000"])
    io.read()
    io.close()
    # MEMO: 良いテスト方法が思いつかないため、現状は呼び出しているだけ

  def test_get_content(self):
    target = DetailPageFetcher.get_content
    content = target(["000000000000"])
    # MEMO: 良いテスト方法が思いつかないため、現状は呼び出しているだけ

if __name__ == "__main__":
  unittest.main()
