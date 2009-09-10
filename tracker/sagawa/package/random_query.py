# -*- coding: utf-8 -*-

import sys
from tracking_number import TrackingNumber
from first_page_fetcher import FirstPageFetcher
from first_page_parser import FirstPageParser
from list_page_fetcher import ListPageFetcher

number_prefix = "6000"

numbers = [TrackingNumber.create_random_number(number_prefix) for i in range(10)]
for number in numbers:
  sys.stderr.write(number + "\n")

page = FirstPageFetcher.get()
data = FirstPageParser.parse(page.content)
state = data["jsf_state_64"]
tree  = data["jsf_tree_64"]

list = ListPageFetcher.get(state, tree, numbers)

f = open("tmp.html", "wb")
f.write(list.content)
f.close()
