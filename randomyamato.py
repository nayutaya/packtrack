# -*- coding: utf-8 -*-

import sys
import time
from tracker import jppost
from tracker.yamato.package.session import Session

for i in range(100):
  numbers = []
  for i in range(10):
    number = jppost.PackageTrackingNumber.create_random_number("5")
    numbers.append(number)
    sys.stderr.write(number + "\n")

  sys.stderr.write("---\n")

  session = Session()
  list = session.get_list(numbers)

  for record in list[u"一覧"]:
    tracking_number = record[u"伝票番号"]
    message         = unicode(record[u"メッセージ"])
    details         = record[u"詳細"]
    if details is not None:
      state = details[-1][u"荷物状況"]
    else:
      state = u"未登録"

    print ("\t".join([tracking_number, state, message])).encode("utf-8")

  time.sleep(1.5)
