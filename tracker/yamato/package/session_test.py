# -*- coding: utf-8 -*-

import unittest

from session import Session

def suite():
  return unittest.TestSuite()
  #return unittest.makeSuite(TestXXX, "test")

if __name__ == "__main__":
  unittest.main()
