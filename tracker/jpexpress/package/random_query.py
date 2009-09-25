# -*- coding: utf-8 -*-

import sys
from tracking_number import TrackingNumber
from session import Session

number_prefix = "3480"

session = Session()

numbers = [TrackingNumber.create_random_number(number_prefix) for i in range(10)]
for number in numbers:
  sys.stderr.write(number + "\n")

list = session.get_list_page(numbers)

f = open("tmp.html", "wb")
f.write(list.content)
f.close()

from list_page_parser import ListPageParser

info = ListPageParser.parse(list.content)
print info
