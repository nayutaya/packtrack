# -*- coding: utf-8 -*-

import urllib
import urllib2
from tracker import jpexpress

if False:
  io = jpexpress.open_first_page()
  page1 = io.read()
  f = open("page1.html", "wb")
  f.write(page1)
  f.close()
else:
  f = open("page1.html", "rb")
  page1 = f.read()
  f.close()

session_id = jpexpress.get_session_id(page1)
print session_id

numbers = ["348012244355", "348011824893", "348011053121"]
print numbers

if True:
  io = jpexpress.open_list_page(session_id, numbers)
  page2 = io.read()
  f = open("page2.html", "wb")
  f.write(page2)
  f.close()
else:
  f = open("page2.html", "rb")
  page2 = f.read()
  f.close()
