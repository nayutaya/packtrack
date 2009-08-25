# -*- coding: utf-8 -*-

import re
import urllib
import urllib2

def create_detail_page_url():
  return "http://toi.kuronekoyamato.co.jp/cgi-bin/tneko"

def create_detail_page_base_params():
  return {
    "number00": "",
    "number01": "",
    "number02": "",
    "number03": "",
    "number04": "",
    "number05": "",
    "number06": "",
    "number07": "",
    "number08": "",
    "number09": "",
    "number10": "",
    "timeid": "",
  }

def create_detail_page_number_params():
  return {
    "number00": "1",
    "number01": "225303520584",
  }

def create_detail_page_request():
  params = create_detail_page_base_params()
  params.update(create_detail_page_number_params())
  print params
  return urllib2.Request(
    url  = create_detail_page_url(),
    data = urllib.urlencode(params))

def open_detail_page():
  request = create_detail_page_request()
  return urllib2.urlopen(request)
