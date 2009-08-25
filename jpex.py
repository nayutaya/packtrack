# -*- coding: utf-8 -*-

from tracker import jpexpress

#print jpexpress.get_first_page_url()
#print jpexpress.create_first_page_request()
io = jpexpress.open_first_page()
print io
print io.read(100)
