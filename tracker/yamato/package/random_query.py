# -*- coding: utf-8 -*-

import sys
import time
from tracking_number import TrackingNumber
from session import Session

number_prefix  = "2497"
query_count    = 2
query_interval = 1.5

session = Session()

for x in xrange(query_count):
  numbers = [TrackingNumber.create_random_number(number_prefix) for i in range(10)]
  for number in numbers:
    sys.stderr.write(number + "\n")

  data    = session.get_list(numbers)
  records = data[u"一覧"]

  for record in records:
    tracking_number = record[u"伝票番号"]
    message         = unicode(record[u"メッセージ"])
    details         = record[u"詳細"]
    if details is not None:
      state = details[-1][u"荷物状況"]
    else:
      state = u"不明"

    print ("\t".join([tracking_number, state, message])).encode("shift-jis")

  time.sleep(query_interval)
