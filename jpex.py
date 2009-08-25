# -*- coding: utf-8 -*-

from tracker import jpexpress

#io = jpexpress.open_first_page()
#page1 = io.read()

#f = open("page1.html", "wb")
#f.write(page1)
#f.close()

f = open("page1.html", "rb")
page1 = f.read()
f.close()

#print page1
session_id = jpexpress.get_session_id(page1)
print session_id

url = jpexpress.create_list_page_url(session_id)
print url

#params = jpexpress.create_list_page_base_params()
#print params

#a = ["a", "b"]
#for x, y in enumerate(a):
#  print (x, y)
#a = [1,2,3]
#print a[:4]

#params2 = jpexpress.create_list_page_number_params(["a","b","c","d","e","a","b","c","d","e","f"])
#print params2

params = jpexpress.create_list_page_params(["a","b","c","d","e","a","b","c","d","e","f"])
print params
