# -*- coding: utf-8 -*-

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

list_page = jppost.PackageListPage(page)
#print list_page

from BeautifulSoup import BeautifulSoup
soup = BeautifulSoup(page)
#print soup.prettify()

#body = soup.body
#def get_response_time(body):
#  table = body("table")[0]
#  tr    = table("tr")[0]
#  td    = tr("td")[0]
#  return td.renderContents().strip()
#print ("time", get_response_time(body))

#for x in body("table", {"align": "center"}):
#  print x

#out = body.prettify()

# 値のない属性はエラーとなるため、値を与える
tds = soup.findAll("td", {"nowrap": None})
for td in tds:
  for i, (key, value) in enumerate(td.attrs):
    if key == "nowrap":
      td.attrs[i] = (key, key)

import xml.etree.ElementTree as etree
html = etree.fromstring(soup.prettify())

#out = soup.prettify()

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
