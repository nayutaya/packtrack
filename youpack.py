# -*- coding: utf-8 -*-

import souplib
from tracker.jppost.package.tracking_number import TrackingNumber
from tracker.jppost.package.session import Session


numbers = []
for i in range(10):
  number = TrackingNumber.create_random_number("31744379")
  numbers.append(number)
print numbers

session = Session()

page = session.get_list_page(numbers)
f = open("page.html", "wb")
f.write(page.content)
f.close()
print page.content

"""
f = open("page.html", "rb")
page = f.read()
f.close()
print page
"""

exit(0)

wellformed = souplib.create_well_formed_html(page)
import xml.etree.ElementTree as etree
html = etree.fromstring(wellformed)


body = html.find("body")

def get_response_time(body):
  table = body.findall("table")[0]
  tr    = table.find("tr")
  td    = tr.find("td")
  return td.text.strip()

print get_response_time(body)

out = etree.tostring(body)

f = open("out.html", "wb")
f.write(out)
f.close()
