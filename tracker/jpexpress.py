# -*- coding: utf-8 -*-

import re
import urllib
import urllib2


def get_first_page_url():
  return "http://info.jpexpress.jp/confirm/confirmIndex.html"

def create_first_page_request():
  return urllib2.Request(
    url = get_first_page_url())

def open_first_page():
  request = create_first_page_request()
  return urllib2.urlopen(request)

def get_session_id(html):
  pattern = re.compile(r"jsessionid=([0-9A-Z]+\.[0-9A-Z]+_[0-9A-Z]+)")
  match   = pattern.search(html)
  if match is not None:
    return match.group(1)
  else:
    return None
