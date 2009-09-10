# -*- coding: utf-8 -*-

import souplib
from tracker.jppost.package.tracking_number import TrackingNumber
from tracker import jppost_old

numbers = []
for i in range(10):
  number = TrackingNumber.create_random_number("31744379")
  numbers.append(number)
print numbers

page = jppost_old.PackageListPage.get_content(numbers)
f = open("page.html", "wb")
f.write(page)
f.close()
print page

f = open("page.html", "rb")
page = f.read()
f.close()
print page

#list_page = jppost_old.PackageListPage(page)
#print list_page

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
