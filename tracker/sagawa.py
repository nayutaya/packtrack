# -*- coding: utf-8 -*-

import re
import urllib
import urllib2


class PackageFirstPage:
  def __init__(self):
    pass

  @classmethod
  def create_url(cls):
    return "http://k2k.sagawa-exp.co.jp/p/sagawa/web/okurijoinput.jsp"

  @classmethod
  def create_request(cls):
    return urllib2.Request(
      url = cls.create_url())

  @classmethod
  def open(cls):
    request = cls.create_request()
    return urllib2.urlopen(request)

  @classmethod
  def get_content(cls):
    io = cls.open()
    page = io.read()
    io.close()
    return page



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
  cls = PackageFirstPage
  html = cls.get_content()
  return parse_first_page_params(html)

def create_detail_page_url():
  return "http://k2k.sagawa-exp.co.jp/p/sagawa/web/okurijoinput.jsp"

def create_detail_page_number_params(numbers):
  num = 1
  result = {}
  for number in numbers:
    result["main:no%i" % num] = number
    num += 1
  return result

def create_detail_page_request(params):
  return urllib2.Request(
    url  = create_detail_page_url(),
    data = urllib.urlencode(params))

def open_detail_page(params):
  request = create_detail_page_request(params)
  return urllib2.urlopen(request)

def get_detail_page(params):
  io = open_detail_page(params)
  page = io.read()
  io.close()
  return page
