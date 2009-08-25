# -*- coding: utf-8 -*-

import re
import urllib
import urllib2


def create_first_page_url():
  return "http://info.jpexpress.jp/confirm/confirmIndex.html"

def create_first_page_request():
  return urllib2.Request(
    url = create_first_page_url())

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

def create_list_page_url(session_id):
  return "http://info.jpexpress.jp/confirm/confirmIndex.html;jsessionid=" + session_id

def create_list_page_base_params():
  return {
    "includeChildBody:confirmIndexForm:doConfirmCareerList": "",
    "includeChildBody:confirmIndexForm/confirm/confirmIndex.html": "includeChildBody:confirmIndexForm",
    "includeChildBody:confirmIndexForm:denpyoNo0": "",
    "includeChildBody:confirmIndexForm:denpyoNo1": "",
    "includeChildBody:confirmIndexForm:denpyoNo2": "",
    "includeChildBody:confirmIndexForm:denpyoNo3": "",
    "includeChildBody:confirmIndexForm:denpyoNo4": "",
    "includeChildBody:confirmIndexForm:denpyoNo5": "",
    "includeChildBody:confirmIndexForm:denpyoNo6": "",
    "includeChildBody:confirmIndexForm:denpyoNo7": "",
    "includeChildBody:confirmIndexForm:denpyoNo8": "",
    "includeChildBody:confirmIndexForm:denpyoNo9": "",
  }

def create_list_page_number_params(numbers):
  params = {}
  for i, number in enumerate(numbers[:10]):
    params["includeChildBody:confirmIndexForm:denpyoNo%i" % i] = number
  return params

def create_list_page_params(numbers):
  params = create_list_page_base_params()
  params.update(create_list_page_number_params(numbers))
  return params
