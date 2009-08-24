# -*- coding: utf-8 -*-

import re
from google.appengine.api import urlfetch


def create_first_page_url():
  return "http://k2k.sagawa-exp.co.jp/p/sagawa/web/okurijoinput.jsp"

def fetch_first_page():
  url = create_first_page_url()
  return urlfetch.fetch(url = url)

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

def get_first_page_params():
  result = fetch_first_page()
  if result.status_code == 200:
    fields = get_input_fields(result.content)
    params = {}
    for field in fields:
      name  = field.get("name")
      value = field.get("value", "")
      params[name] = value
    return params
  return None
