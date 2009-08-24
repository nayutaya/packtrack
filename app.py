# -*- coding: utf-8 -*-

import re
import logging
import urllib
from google.appengine.api import urlfetch

import tracker.sagawa


print "Content-Type: text/plain"
#print "Content-Type: text/html"
print ""

#print "hello"

result = tracker.sagawa.get_first_page()

print result.status_code
#print result.content

#print tracker.sagawa.parse_forms(result.content)
fields = tracker.sagawa.get_input_fields(result.content)
for field in fields:
  print field

exit(0)


input_fragments = get_input_fragments(result.content)
input_fields    = get_input_fields(input_fragments)
#for input_fragment in input_fragments:
#  print input_fragment
"""
print "----------"
for input_field in input_fields:
  print input_field
"""

#print "----------"
hash = {}
for input_field in input_fields:
  name  = input_field.get("name")
  value = input_field.get("value", "")
  hash[name] = value
#print hash


hash["main:no1"] = "600097281033"
hash["main:no2"] = "600092368315"

url = "http://k2k.sagawa-exp.co.jp/p/sagawa/web/okurijoinput.jsp"
data = urllib.urlencode(hash)
result = urlfetch.fetch(url = url, method = urlfetch.POST, payload = data)

#print "----------"
#print result.status_code
print result.content
