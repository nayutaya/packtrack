# -*- coding: utf-8 -*-

import re
import logging
import urllib
from google.appengine.api import urlfetch

from tracker import sagawa


"""
def sagawa():
  numbers = [
    "600097281033",
    "600092368315"
  ]

  params = sagawa.get_first_page_params()
  params.update(sagawa.create_detail_page_number_params(numbers))
  #print params

  result = sagawa.fetch_detail_page(params)
  #print result.status_code
  print result.content
"""


def get_first_page_url():
  return "http://info.jpexpress.jp/confirm/confirmIndex.html"

def fetch_first_page():
  return urlfetch.fetch(
    method = urlfetch.GET,
    url    = get_first_page_url())

print "Content-Type: text/plain"
#print "Content-Type: text/html"
print ""

result = fetch_first_page()
#print result.status_code
#print result.content

pattern = re.compile(r"action=\"(.+?)\"", re.IGNORECASE)
match = pattern.search(result.content)
path = match.group(1)
#print path

url = "http://info.jpexpress.jp" + path
#print url

#url = "https://info.jpexpress.jp:443/confirm/confirmList.html"

params = {
  "includeChildBody:confirmIndexForm:doConfirmCareerList": "",
  "includeChildBody:confirmIndexForm/confirm/confirmIndex.html": "includeChildBody:confirmIndexForm",
  "includeChildBody:confirmIndexForm:denpyoNo0": "348012244355",
  "includeChildBody:confirmIndexForm:denpyoNo1": "348011824893",
  "includeChildBody:confirmIndexForm:denpyoNo2": "",
  "includeChildBody:confirmIndexForm:denpyoNo3": "",
  "includeChildBody:confirmIndexForm:denpyoNo4": "",
  "includeChildBody:confirmIndexForm:denpyoNo5": "",
  "includeChildBody:confirmIndexForm:denpyoNo6": "",
  "includeChildBody:confirmIndexForm:denpyoNo7": "",
  "includeChildBody:confirmIndexForm:denpyoNo8": "",
  "includeChildBody:confirmIndexForm:denpyoNo9": "",
}
#print hash
#print urllib.urlencode(params)


result = urlfetch.fetch(
  method  = urlfetch.POST,
  url     = url,
  payload = urllib.urlencode(params),
  follow_redirects = False)
#print result
#print result.status_code
print result.content

#print "----------"

url = result.headers["location"]
#print url
pattern = re.compile(r"\?.*$")
url = pattern.sub("", url)
print url

result = urlfetch.fetch(
  #method = urlfetch.POST,
  url    = url)
#print result
#print result.headers
print result.status_code
print result.content
