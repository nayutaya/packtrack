# -*- coding: utf-8 -*-

import re
from tracker import jpexpress

if False:
  page1 = jpexpress.PackageFirstPage.get()
  f = open("page1.html", "wb")
  f.write(page1.content)
  f.close()
else:
  f = open("page1.html", "rb")
  page1 = jpexpress.PackageFirstPage(f.read())
  f.close()

session_id = page1.get_jsession_id()
print session_id


numbers = ["348012244355", "348011824893", "348011053121"]
print numbers

if False:
  page2 = jpexpress.PackageListPage.get(session_id, numbers)
  f = open("page2.html", "wb")
  f.write(page2.content)
  f.close()
else:
  f = open("page2.html", "rb")
  page2 = jpexpress.PackageListPage(f.read())
  f.close()

"""
pattern = re.compile(r"href=\"confirmDetail\.html;.+?\?(.+?)\"")
for params in pattern.findall(page2.content):
  params2 = re.compile(r"&amp;").sub("&", params)
  print "---"
  print jpexpress.PackageDetailPage.create_url(session_id, params2)
"""

"""
import souplib
page = souplib.create_well_formed_html(page2.content)
f = open("page.html", "wb")
f.write(page)
f.close()
import xml.etree.ElementTree as etree
html = etree.fromstring(page)
"""

from BeautifulSoup import BeautifulSoup
soup = BeautifulSoup(page2.content)

def get_list_table(soup):
  for elem1 in soup.findAll("div", {"id": "isGetData"}):
    for elem2 in elem1.findAll("table"):
      return elem2
  return None

list_table = get_list_table(soup)

print list_table.prettify()
