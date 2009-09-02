# -*- coding: utf-8 -*-

from tracker.yamato.package.detail_page_fetcher import DetailPageFetcher
from tracker.yamato.package.detail_page_parser import DetailPageParser

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


#print detail_page

from BeautifulSoup import BeautifulSoup

import re
def strip_javascript(html):
  pattern = re.compile(r"<script.+?>.+?</script>", re.DOTALL)
  return re.sub(pattern, "", html)

src1 = detail_page
src2 = strip_javascript(src1)

#f = open("tmp.html", "wb")
#f.write(src2)
#f.close()

doc = BeautifulSoup(src2)

f = open("tmp.html", "wb")
f.write(doc.prettify())
f.close()
