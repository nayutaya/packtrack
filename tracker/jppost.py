# -*- coding: utf-8 -*-

import urllib
import urllib2


def create_list_page_base_params():
  return {
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

def create_list_page_number_params(numbers):
  params = {}
  for i, number in enumerate(numbers[:10]):
    params["reqCodeNo%i" % (i + 1)] = number
  return params

def create_list_page_params(numbers):
  params = create_list_page_base_params()
  params.update(create_list_page_number_params(numbers))
  return params

def create_list_page_base_url():
  return "http://tracking.post.japanpost.jp/service/singleSearch.do"

def create_list_page_url(numbers):
  base   = create_list_page_base_url()
  params = create_list_page_params(numbers)
  return base + "?" + urllib.urlencode(params)

def create_list_page_request(numbers):
  return urllib2.Request(
    url = create_list_page_url(numbers))

def open_list_page(numbers):
  request = create_list_page_request(numbers)
  return urllib2.urlopen(request)

def get_list_page(numbers):
  io = open_list_page(numbers)
  page = io.read()
  io.close()
  return page
