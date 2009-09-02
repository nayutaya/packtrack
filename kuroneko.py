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

def strip_center_tag(html):
  pattern = re.compile(r"</?center>", re.IGNORECASE)
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

src4 = strip_center_tag(src3)
f = open("src4.html", "wb")
f.write(src4)
f.close()

doc = BeautifulSoup(src4)
f = open("tmp.html", "wb")
f.write(doc.prettify())
f.close()

# ヘッダを削除
for i in range(4):
  doc.body.table.extract()
doc.body.form.extract()
for i in range(4):
  doc.body.table.extract()

# フッタを削除
doc.body.findAll("p", recursive = False)[-1].extract()

# リンクを削除
for elem in doc.body.findAll("a", {"name": re.compile(".+")}):
  elem.extract()
for elem in doc.body.findAll("p", {"align": "right"}):
  elem.extract()

f = open("tmp2.html", "wb")
f.write(doc.prettify())
f.close()

# ボタンを削除
for elem in doc.body.findAll("div", {"class": "print_hide"}):
  elem.extract()

# 水平線を削除
for elem in doc.body.findAll("hr"):
  elem.extract()

#for elem in doc.body.findAll("center"):
#  #elem.extract()
#  print elem

f = open("tmp3.html", "wb")
f.write(doc.prettify())
f.close()
