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


class PackageDetailPage:
  def __init__(self):
    pass

  @classmethod
  def create_detail_page_url(cls):
    return "http://k2k.sagawa-exp.co.jp/p/sagawa/web/okurijoinput.jsp"

  @classmethod
  def create_detail_page_base_params(cls):
    return {
      "jsf_viewid": "/web/okurijoinput.jsp",
      "main:_link_hidden_": "",
      "main:correlation": "1",
      "main:no1": "",
      "main:no2": "",
      "main:no3": "",
      "main:no4": "",
      "main:no5": "",
      "main:no6": "",
      "main:no7": "",
      "main:no8": "",
      "main:no9": "",
      "main:no10": "",
      "main_SUBMIT": "1",
      "main:toiStart": "",
    }

  @classmethod
  def create_detail_page_system_params(cls, state, tree):
    return {
      "jsf_state_64": state,
      "jsf_tree_64": tree,
    }

  @classmethod
  def create_detail_page_number_params(cls, numbers):
    params = {}
    for i, number in enumerate(numbers[:10]):
      params["main:no%i" % (i + 1)] = number
    return params

  @classmethod
  def create_params(cls, state, tree, numbers):
    params = cls.create_detail_page_base_params()
    params.update(cls.create_detail_page_system_params(state, tree))
    params.update(cls.create_detail_page_number_params(numbers))
    return params


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



def create_detail_page_request(params):
  cls = PackageDetailPage
  return urllib2.Request(
    url  = cls.create_detail_page_url(),
    data = urllib.urlencode(params))

def open_detail_page(params):
  request = create_detail_page_request(params)
  return urllib2.urlopen(request)

def get_detail_page(params):
  io = open_detail_page(params)
  page = io.read()
  io.close()
  return page
