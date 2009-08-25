# -*- coding: utf-8 -*-

from tracker import jpexpress

if False:
  io = jpexpress.open_first_page()
  page1 = io.read()
  f = open("page1.html", "wb")
  f.write(page1)
  f.close()
else:
  f = open("page1.html", "rb")
  page1 = f.read()
  f.close()

session_id = jpexpress.get_session_id(page1)
print session_id

#url = jpexpress.create_list_page_url(session_id)
#print url

numbers = ["348012244355", "348011824893", "348011053121"]
#params = jpexpress.create_list_page_params(numbers)
#print params

import urllib
import urllib2
#data = urllib.urlencode(params)
#print data

#req = urllib2.Request(
#  url = url, data = data)
#print req

req = jpexpress.create_list_page_request(session_id, numbers)
io = urllib2.urlopen(req)
print io.info()
page2 = io.read()

if True:
  f = open("page2.html", "wb")
  f.write(page2)
  f.close()
