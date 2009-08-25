# -*- coding: utf-8 -*-

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
