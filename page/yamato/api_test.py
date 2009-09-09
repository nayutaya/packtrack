# -*- coding: utf-8 -*-

import unittest

from api import ListParameter

class TestListParameter(unittest.TestCase):
  def setUp(self):
    pass

  def test_parse_numbers(self):
    target = ListParameter.parse_numbers

    self.assertEqual([], target(None))
    self.assertEqual([], target(""))

    self.assertEqual(["1"], target("1"))
    self.assertEqual(["1"], target("1,"))
    self.assertEqual(["1", "2"], target("1,2"))
    self.assertEqual(["1", "2"], target("1,2,"))


if __name__ == "__main__":
  unittest.main()
