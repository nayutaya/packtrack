# -*- coding: utf-8 -*-

from tracker.yamato.package.session import Session
#from tracker.yamato.package.detail_page_fetcher import DetailPageFetcher
#from tracker.yamato.package.detail_page_parser import DetailPageParser


session = Session()
print session.get_list(["225303520584", "249790484403"])

exit(0)

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

info = DetailPageParser.parse(html)
for item1 in info[u"一覧"]:
  for key1, value1 in item1.items():
    if isinstance(value1, basestring):
      print key1 + ": '" + value1 + "'"
    else:
      print key1 + ":"
      for item2 in value1:
        for key2, value2 in item2.items():
          print "  " + key2 + ": '" + value2 + "'"
        print "  ---"
  print "---"
