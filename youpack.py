# -*- coding: utf-8 -*-

from tracker import jppost

#print jppost.create_list_page_url()
#print jppost.create_list_page_request()
#print jppost.open_list_page()

#print jppost.PackageTrackingNumber.create_check_digit("31744379420")

numbers = []
for i in range(10):
  number = jppost.PackageTrackingNumber.create_random_number("3174")
  numbers.append(number)
print numbers

#numbers = [
#  "317443794205",
#  "317443794334",
#]

page = jppost.PackageListPage.get_content(numbers)
f = open("page.html", "wb")
f.write(page)
f.close()
#print page
