# -*- coding: utf-8 -*-

import sys
from tracker import jpexpress

session = jpexpress.PackageTrackingSession()
#print session

#numbers = ["348012244355", "348011824893", "348011053121"]

for i in range(5):
  sys.stderr.write(".")

  from tracker import jppost
  numbers = []
  for i in range(10):
    number = jppost.PackageTrackingNumber.create_random_number("3480")
    numbers.append(number)

  page = session.get_list_page(numbers)
  #print page
  f = open("page2.html", "wb")
  f.write(page.content)
  f.close()

  page_info = jpexpress.PackageListPageParser.parse(page.content)
  #print page_info

  for record in page_info["list"]:
    line  = ""
    line += (record[u"No"]                 ) + "\t"
    line += (record[u"送り状番号"]         ) + "\t"
    line += (record[u"最新状況"]      or "") + "\t"
    line += (record[u"最新状況:日時"] or "") + "\t"
    line += (record[u"受付日"]        or "") + "\t"
    line += (record[u"お届け指定日"]  or "") + "\t"
    line += (record[u"扱区分"]        or "")
    print line.encode("shift-jis")
