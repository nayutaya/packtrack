# -*- coding: utf-8 -*-

import re
import logging
import urllib
from google.appengine.api import urlfetch

import tracker.sagawa


#print "Content-Type: text/plain"
print "Content-Type: text/html"
print ""

#print "hello"

url    = "http://k2k.sagawa-exp.co.jp/p/sagawa/web/okurijoinput.jsp"
result = urlfetch.fetch(url = url)

#print result.status_code
#print result.content

#regexp = re.compile(r"<input type=\"hidden\" name=\"jsf_tree_64\".+value=\".+?\"", re.IGNORECASE | re.DOTALL)
#match  = regexp.search(result.content)
#print match
#print match.group(0)

def get_input_fragments(src):
  regexp = re.compile(r"<input.+?>", re.IGNORECASE | re.DOTALL)
  return regexp.findall(src)

def get_input_fields(fragments):
  pattern = re.compile(r" (.*?)=\"(.*?)\"")

  results = []
  for fragment in fragments:
    hash = {}
    for key, value in pattern.findall(fragment):
      hash[key] = value
    results.append(hash)

  return results

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
