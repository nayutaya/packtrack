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
def strip_script_tag(html):
  pattern = re.compile(r"<script.+?>.+?</script>", re.IGNORECASE | re.DOTALL)
  return re.sub(pattern, "", html)

def strip_style_tag(html):
  pattern = re.compile(r"<style.+?>.+?</style>", re.IGNORECASE | re.DOTALL)
  return re.sub(pattern, "", html)



src1 = detail_page
f = open("src1.html", "wb")
f.write(src1)
f.close()

src2 = strip_script_tag(src1)
f = open("src2.html", "wb")
f.write(src2)
f.close()

src3 = strip_style_tag(src2)
f = open("src3.html", "wb")
f.write(src3)
f.close()

doc = BeautifulSoup(src3)
f = open("tmp.html", "wb")
f.write(doc.prettify())
f.close()

doc.body.center.extract()
doc.body.center.extract()

for elem in doc.body.findAll("a", recursive = False):
  elem.extract()

f = open("tmp2.html", "wb")
f.write(doc.prettify())
f.close()

for elem in doc.body.findAll("div", {"class": "print_hide"}):
  elem.extract()

for elem in doc.body.findAll("p", {"align": "right"}):
  elem.extract()

f = open("tmp3.html", "wb")
f.write(doc.prettify())
f.close()
