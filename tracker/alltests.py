# -*- coding: utf-8 -*-

import unittest

import jpexpress.alltests
import yamato.alltests

def suite():
  suites = [
    jpexpress.alltests.suite(),
    yamato.alltests.suite(),
  ]
  return unittest.TestSuite(suites)

if __name__ == "__main__":
  unittest.TextTestRunner(verbosity = 1).run(suite())
