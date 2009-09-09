# -*- coding: utf-8 -*-

import unittest

import package.alltests

def suite():
  suites = [
    package.alltests.suite(),
  ]
  return unittest.TestSuite(suites)

if __name__ == "__main__":
  unittest.TextTestRunner(verbosity = 1).run(suite())
