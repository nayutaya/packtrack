# -*- coding: utf-8 -*-

import re
from tracker import jpexpress

session = jpexpress.PackageTrackingSession()
print session

#numbers = ["348012244355", "348011824893", "348011053121"]

from tracker import jppost
numbers = []
for i in range(10):
  number = jppost.PackageTrackingNumber.create_random_number("3480")
  numbers.append(number)

page = session.get_list_page(numbers)
print page
f = open("page2.html", "wb")
f.write(page.content)
f.close()

page_info = jpexpress.PackageListPageParser.parse(page.content)
print page_info
