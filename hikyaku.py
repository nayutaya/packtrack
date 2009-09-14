# -*- coding: utf-8 -*-

from tracker.sagawa.package.session import Session

numbers = [
  "600097281033",
  "600092368315"
]

session = Session()

list = session.get_list_page(numbers)
print list.content
