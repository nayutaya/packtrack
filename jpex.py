# -*- coding: utf-8 -*-

from tracker import jpexpress

#print jpexpress.get_first_page_url()
#print jpexpress.create_first_page_request()
#io = jpexpress.open_first_page()
#page1 = io.read()

#f = open("page1.html", "wb")
#f.write(page1)
#f.close()

f = open("page1.html", "rb")
page1 = f.read()
f.close()

#print page1
print jpexpress.get_session_id(page1)
