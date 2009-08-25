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

body = soup.body

table = body("table", {"align": "center"})[0]
tr    = table("tr")[0]
td    = tr("td")[0]
print td.renderContents().strip()

#for x in body("table", {"align": "center"}):
#  print x

out = body.prettify()
f = open("out.html", "wb")
f.write(out)
f.close()
