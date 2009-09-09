# -*- coding: utf-8 -*-

import unittest

import list_page_fetcher_test
import list_page_parser_test
import session_test
import tracking_number_test

def suite():
  loader = unittest.defaultTestLoader.loadTestsFromModule
  suites = [
    loader(list_page_fetcher_test),
    loader(list_page_parser_test),
    loader(session_test),
    loader(tracking_number_test),
  ]
  return unittest.TestSuite(suites)

if __name__ == "__main__":
  unittest.TextTestRunner(verbosity = 1).run(suite())
