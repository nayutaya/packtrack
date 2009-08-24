# -*- coding: utf-8 -*-

import re
from google.appengine.api import urlfetch


def create_first_page_url():
  return "http://k2k.sagawa-exp.co.jp/p/sagawa/web/okurijoinput.jsp"

def get_first_page():
  url = create_first_page_url()
  return urlfetch.fetch(url = url)

#def parse_forms(html):
#  pattern = re.compile(r"<form(.*?)>(.*?)</form>", re.IGNORECASE | re.DOTALL)
#  return pattern.findall(html)

def get_input_fields(html):
  pattern = re.compile(r"<input(.+?)>", re.IGNORECASE | re.DOTALL)

  results = []
  for fragment in pattern.findall(html):
    attrs = parse_attributes(fragment)
    results.append(attrs)

  return results

def parse_attributes(html):
  pattern = re.compile(r" (.+?)=\"(.+?)\"")

  result = {}
  for key, value in pattern.findall(html):
    result[key] = value

  return result
