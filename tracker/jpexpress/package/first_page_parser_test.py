# -*- coding: utf-8 -*-

import unittest

from first_page_parser import FirstPageParser

class TestFirstPageParser(unittest.TestCase):
  def setUp(self):
    pass

  def test_parse(self):
    target = FirstPageParser.parse

    src = open("fixtures/first.html", "rb").read()
    expected = {
      "jsessionid": "39A6C0TBKUFKR11NTUM7N3FKKDGU03V05N0I3F5FMQMFFB9I23PKAAF9B4HG2000JO000000.WU001_001",
    }
    self.assertEqual(expected, target(src))

if __name__ == "__main__":
  unittest.main()
