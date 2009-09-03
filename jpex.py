# -*- coding: utf-8 -*-

import sys
import time
from tracker.jpexpress.package.tracking_number import TrackingNumber
from tracker.jpexpress.package.session import Session

session = Session()
#print session

numbers = [
  "348012244355",
  "348011824893",
  "348011053121",
]

for i in range(100):
  if True:
    from tracker import jppost
    numbers = []
    for i in range(10):
      number = jppost.PackageTrackingNumber.create_random_number("")
      numbers.append(number)
      sys.stderr.write(number + "\n")

  page_info = session.get_list(numbers)

  for record in page_info[u"一覧"]:
    sys.stderr.write(".")
    line  = ""
    line += (record[u"送り状番号"]         ) + "\t"
    line += (record[u"最新状況"]      or "") + "\t"
    line += (record[u"最新状況:日時"] or "") + "\t"
    line += (record[u"受付日"]        or "") + "\t"
    line += (record[u"お届け指定日"]  or "") + "\t"
    line += (record[u"扱区分"]        or "")
    print line.encode("shift-jis")

    number = record[u"送り状番号"]
    params = record[u"送り状番号:パラメータ"]
    if params is not None:
      detail_page = session.get_detail(params)
      #print detail_page
      for key, value in detail_page.items():
        print ("  " + key + ": " + value).encode("shift-jis")

  time.sleep(1.5)
