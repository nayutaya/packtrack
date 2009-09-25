# -*- coding: utf-8 -*-

import sys
from tracking_number import TrackingNumber
from session import Session

number_prefix = "3480"

session = Session()

numbers = [TrackingNumber.create_random_number(number_prefix) for i in range(10)]
for number in numbers:
  sys.stderr.write(number + "\n")

data    = session.get_list(numbers)
records = data[u"一覧"]

for record in records:
  tracking_number = record[u"送り状番号"]
  state           = unicode(record[u"最新状況"])

  print ("\t".join([tracking_number, state])).encode("shift-jis")
