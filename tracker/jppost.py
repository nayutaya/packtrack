# -*- coding: utf-8 -*-

import urllib
import urllib2


def create_list_page_base_params():
  return {
    "JSESSIONID": "KTzQblRXyvQWJh1BzkTm3YZzyszpMwyYf81fSpZypTVGjQVLLdkK!1995213173!1251210176530",
    "org.apache.struts.taglib.html.TOKEN": "825c0b1b950dbb316bcd2c66576e42e7",
    "SVID": "020",
    "locale": "ja",
    "searchKind": "S002",
    "reqCodeNo1": "",
    "reqCodeNo2": "",
    "reqCodeNo3": "",
    "reqCodeNo4": "",
    "reqCodeNo5": "",
    "reqCodeNo6": "",
    "reqCodeNo7": "",
    "reqCodeNo8": "",
    "reqCodeNo9": "",
    "reqCodeNo10": "",
  }

def create_list_page_number_params():
  return {
    "reqCodeNo1": "317443794205",
    "reqCodeNo2": "317443794334",
  }

def create_list_page_params():
  params = create_list_page_base_params()
  params.update(create_list_page_number_params())
  return params

def create_list_page_base_url():
  return "http://tracking.post.japanpost.jp/service/singleSearch.do"

def create_list_page_url():
  base   = create_list_page_base_url()
  params = create_list_page_params()
  return base + "?" + urllib.urlencode(params)

def create_list_page_request():
  return urllib2.Request(
    url = create_list_page_url())

def open_list_page():
  request = create_list_page_request()
  return urllib2.urlopen(request)

def get_list_page():
  io = open_list_page()
  page = io.read()
  io.close()
  return page
