# -*- coding: utf-8 -*-

import re
import logging
import urllib
from google.appengine.api import urlfetch

from tracker import sagawa


print "Content-Type: text/plain"
#print "Content-Type: text/html"
print ""

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


def get_first_page_url():
  return "http://info.jpexpress.jp/confirm/confirmIndex.html"

def fetch_first_page():
  return urlfetch.fetch(
    method = urlfetch.GET,
    url    = get_first_page_url())

result = fetch_first_page()
#print result.status_code
#print result.content

pattern = re.compile(r"action=\"(.+?)\"", re.IGNORECASE)
match = pattern.search(result.content)
path = match.group(1)
print path

url = "http://info.jpexpress.jp" + path
print url

#url = "https://info.jpexpress.jp:443/confirm/confirmList.html;jsessionid=ECV69VR99S9333NAB6M965QG21GU03V05N0I3F4IONCKO23N797DA6GG9KHG200048000000.WU001_004?te-uniquekey=1234d109b1a"
#url = "https://info.jpexpress.jp:443/confirm/confirmList.html"

params = {
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

headers = {
  #"Referer": "http://info.jpexpress.jp/confirm/confirmIndex.html",
  #"Referrer": "http://info.jpexpress.jp/confirm/confirmIndex.html",
  #"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.0; ja; rv:1.9.0.13) Gecko/2009073022 Firefox/3.0.13 (.NET CLR 3.5.30729) AutoPager/0.5.2.2 (http://www.teesoft.info/)",
  #"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
  #"Accept-Language": "ja,en-us;q=0.7,en;q=0.3",
  #"Accept-Encoding": "gzip,deflate",
  #"Accept-Charset": "Shift_JIS,utf-8;q=0.7,*;q=0.7",
  #"Keep-Alive": "300",
  #"Connection": "keep-alive",
}

result = urlfetch.fetch(
  method = urlfetch.POST,
  url    = url,
  payload = urllib.urlencode(params), headers = headers, follow_redirects = False)
#print result
print result.status_code
#print result.content
