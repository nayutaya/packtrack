# -*- coding: utf-8 -*-

from tracker.yamato.package.detail_page_fetcher import DetailPageFetcher
from tracker.yamato.package.detail_page_parser import DetailPageParser

"""
if False:
  numbers = ["225303520584", "249790484403"]
  detail_page = DetailPageFetcher.get_content(numbers)
  f = open("yamato.html", "wb")
  f.write(detail_page)
  f.close()
else:
  f = open("yamato.html", "rb")
  detail_page = f.read()
  f.close()
"""

import re
from BeautifulSoup import BeautifulSoup

f = open("tracker/yamato/package/fixtures/detail_count02.html", "rb")
html = f.read()
f.close()
#print html

doc = DetailPageParser.create_doc(html)
f = open("tmp.html", "wb")
f.write(doc.prettify())
f.close()


elements = DetailPageParser.search_tracking_number_elements(doc)
for elem in elements:
  print elem
  print elem.nextSibling.nextSibling
