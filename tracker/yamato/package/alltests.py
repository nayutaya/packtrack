# -*- coding: utf-8 -*-

import unittest

import list_page_fetcher_test
import list_page_parser_test
import session_test
import tracking_number_test

suite = unittest.TestSuite()
suite.addTest(list_page_fetcher_test.suite())
suite.addTest(list_page_parser_test.suite())
suite.addTest(session_test.suite())
suite.addTest(tracking_number_test.suite())

unittest.TextTestRunner(verbosity = 1).run(suite)
