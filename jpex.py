# -*- coding: utf-8 -*-

import re
import urllib
import urllib2
from tracker import jpexpress

if True:
  page1 = jpexpress.PackageFirstPage.get()
  f = open("page1.html", "wb")
  f.write(page1.content)
  f.close()
else:
  f = open("page1.html", "rb")
  page1 = f.read()
  f.close()

session_id = page1.get_jsession_id()
print session_id


numbers = ["348012244355", "348011824893", "348011053121"]
print numbers

if True:
  page2 = jpexpress.PackageListPage.get_content(session_id, numbers)
  f = open("page2.html", "wb")
  f.write(page2)
  f.close()
else:
  f = open("page2.html", "rb")
  page2 = f.read()
  f.close()

pattern = re.compile(r"href=\"confirmDetail\.html;.+?\?(.+?)\"")

for params in pattern.findall(page2):
  params2 = re.compile(r"&amp;").sub("&", params)
  print "---"
  print jpexpress.create_detail_page_url(session_id, params2)
