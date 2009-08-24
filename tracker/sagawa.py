# -*- coding: utf-8 -*-

import re
import urllib
from google.appengine.api import urlfetch


def create_first_page_url():
  return "http://k2k.sagawa-exp.co.jp/p/sagawa/web/okurijoinput.jsp"

def fetch_first_page():
  return urlfetch.fetch(
    method = urlfetch.GET,
    url    = create_first_page_url())

def get_input_fields(html):
  pattern = re.compile(r"<input(.+?)>", re.IGNORECASE | re.DOTALL)

  results = []
  for fragment in pattern.findall(html):
    attrs = parse_attributes(fragment)
    results.append(attrs)

  return results

def parse_attributes(html):
  pattern = re.compile(r" (.+?)=\"(.*?)\"")

  result = {}
  for key, value in pattern.findall(html):
    result[key] = value

  return result

def parse_first_page_params(html):
  params = {}
  for field in get_input_fields(html):
    name  = field.get("name")
    value = field.get("value", "")
    params[name] = value
  return params

def get_first_page_params():
  result = fetch_first_page()
  if result.status_code == 200:
    return parse_first_page_params(result.content)
  else:
    return None

def create_detail_page_url():
  return "http://k2k.sagawa-exp.co.jp/p/sagawa/web/okurijoinput.jsp"

def create_detail_page_number_params(numbers):
  num = 1
  result = {}
  for number in numbers:
    result["main:no%i" % num] = number
    num += 1
  return result

def fetch_detail_page(params):
  return urlfetch.fetch(
    method  = urlfetch.POST,
    url     = create_detail_page_url(),
    payload = urllib.urlencode(params))
