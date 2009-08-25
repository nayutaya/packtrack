# -*- coding: utf-8 -*-

import re
import urllib
import urllib2


def create_detail_page_url():
  return "http://toi.kuronekoyamato.co.jp/cgi-bin/tneko"

def create_detail_page_base_params():
  return {
    "number00": "1",
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

def create_detail_page_number_params(numbers):
  params = {}
  for i, number in enumerate(numbers[:10]):
    params["number%02i" % (i + 1)] = number
  return params

def create_detail_page_params(numbers):
  params = create_detail_page_base_params()
  params.update(create_detail_page_number_params(numbers))
  return params

def create_detail_page_request(numbers):
  params = create_detail_page_params(numbers)
  return urllib2.Request(
    url  = create_detail_page_url(),
    data = urllib.urlencode(params))

def open_detail_page(numbers):
  request = create_detail_page_request(numbers)
  return urllib2.urlopen(request)

def get_detail_page(numbers):
  io = open_detail_page(numbers)
  page = io.read()
  io.close()
  return page
