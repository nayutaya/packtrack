# -*- coding: utf-8 -*-

import re
import urllib
import urllib2
from BeautifulSoup import BeautifulSoup


class PackageFirstPage:
  def __init__(self, content):
    self.content  = content
    self.jsfstate = None
    self.jsftree  = None

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

  @classmethod
  def get(cls):
    return cls(cls.get_content())

  def get_jsfstate(self):
    if self.jsfstate is None:
      self.parse_content()
    return self.jsfstate

  def get_jsftree(self):
    if self.jsftree is None:
      self.parse_content()
    return self.jsftree

  def parse_content(self):
    hidden_fields = {}

    soup = BeautifulSoup(self.content)
    for field in soup.findAll("input", {"type": "hidden"}):
      field_name, field_value = None, None
      for (attr_name, attr_value) in field.attrs:
        if   attr_name == "name" : field_name  = attr_value
        elif attr_name == "value": field_value = attr_value
      hidden_fields[field_name] = field_value

    self.jsfstate = hidden_fields["jsf_state_64"]
    self.jsftree  = hidden_fields["jsf_tree_64"]

class PackageDetailPage:
  def __init__(self):
    pass

  @classmethod
  def create_url(cls):
    return "http://k2k.sagawa-exp.co.jp/p/sagawa/web/okurijoinput.jsp"

  @classmethod
  def create_base_params(cls):
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
  def create_system_params(cls, state, tree):
    return {
      "jsf_state_64": state,
      "jsf_tree_64": tree,
    }

  @classmethod
  def create_number_params(cls, numbers):
    params = {}
    for i, number in enumerate(numbers[:10]):
      params["main:no%i" % (i + 1)] = number
    return params

  @classmethod
  def create_params(cls, state, tree, numbers):
    params = cls.create_base_params()
    params.update(cls.create_system_params(state, tree))
    params.update(cls.create_number_params(numbers))
    return params

  @classmethod
  def create_request(cls, params):
    return urllib2.Request(
      url  = cls.create_url(),
      data = urllib.urlencode(params))

  @classmethod
  def open(cls, params):
    request = cls.create_request(params)
    return urllib2.urlopen(request)

  @classmethod
  def get_content(cls, params):
    io = cls.open(params)
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
