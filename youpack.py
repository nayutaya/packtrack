# -*- coding: utf-8 -*-

from tracker import jppost

#print jppost.create_list_page_url()
#print jppost.create_list_page_request()
#print jppost.open_list_page()

numbers = [
  "317443794205",
  "317443794334",
]

page = jppost.get_list_page(numbers)
f = open("page.html", "wb")
f.write(page)
f.close()
#print page
