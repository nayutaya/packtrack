# -*- coding: utf-8 -*-

from tracker import jppost
from tracker.yamato.package.session import Session

numbers = []
for i in range(10):
  number = jppost.PackageTrackingNumber.create_random_number("2497")
  numbers.append(number)
  print number

session = Session()
list = session.get_list(numbers)

for record in list[u"一覧"]:
  tracking_number = record[u"伝票番号"]
  message         = record[u"メッセージ"]
  print ("\t".join([tracking_number, message])).encode("utf-8")
