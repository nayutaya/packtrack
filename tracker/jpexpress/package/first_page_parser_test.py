# -*- coding: utf-8 -*-

import unittest
import os

from first_page_parser import FirstPageParser

class TestFirstPageParser(unittest.TestCase):
  def setUp(self):
    pass

  def read_fixture(self, filename):
    path = os.path.join(os.path.dirname(__file__), "fixtures", filename)
    io = open(path, "rb")
    try:
      return io.read()
    finally:
      io.close()

  def test_parse(self):
    target = FirstPageParser.parse

    src = self.read_fixture("first.html")
    expected = {
      "jsessionid": "39A6C0TBKUFKR11NTUM7N3FKKDGU03V05N0I3F5FMQMFFB9I23PKAAF9B4HG2000JO000000.WU001_001",
    }
    self.assertEqual(expected, target(src))

if __name__ == "__main__":
  unittest.main()
