# -*- coding: utf-8 -*-

import urllib
import urllib2
from BeautifulSoup import BeautifulSoup


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
  def create_request(cls, state, tree, numbers):
    params = cls.create_params(state, tree, numbers)
    return urllib2.Request(
      url  = cls.create_url(),
      data = urllib.urlencode(params))

  @classmethod
  def open(cls, state, tree, numbers):
    request = cls.create_request(state, tree, numbers)
    return urllib2.urlopen(request)

  @classmethod
  def get_content(cls, state, tree, numbers):
    io = cls.open(state, tree, numbers)
    try:
      return io.read()
    finally:
      io.close()
