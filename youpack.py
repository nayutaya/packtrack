# -*- coding: utf-8 -*-

import souplib
from tracker import jppost

#print jppost.PackageTrackingNumber.create_check_digit("31744379420")

"""
numbers = []
for i in range(10):
  number = jppost.PackageTrackingNumber.create_random_number("31744379")
  numbers.append(number)
print numbers

page = jppost.PackageListPage.get_content(numbers)
f = open("page.html", "wb")
f.write(page)
f.close()
print page
"""

f = open("page.html", "rb")
page = f.read()
f.close()
#print page

#list_page = jppost.PackageListPage(page)
#print list_page


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
