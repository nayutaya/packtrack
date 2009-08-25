# -*- coding: utf-8 -*-

import urllib
import urllib2


class PackageListPage:
  def __init__(self):
    pass

  @classmethod
  def create_base_params(cls):
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

  @classmethod
  def create_number_params(cls, numbers):
    params = {}
    for i, number in enumerate(numbers[:10]):
      params["reqCodeNo%i" % (i + 1)] = number
    return params

  @classmethod
  def create_list_page_params(cls, numbers):
    params = cls.create_base_params()
    params.update(cls.create_number_params(numbers))
    return params

  @classmethod
  def create_list_page_base_url(cls):
    return "http://tracking.post.japanpost.jp/service/singleSearch.do"

  @classmethod
  def create_list_page_url(cls, numbers):
    base   = cls.create_list_page_base_url()
    params = cls.create_list_page_params(numbers)
    return base + "?" + urllib.urlencode(params)

  @classmethod
  def create_list_page_request(cls, numbers):
    return urllib2.Request(
      url = cls.create_list_page_url(numbers))

  @classmethod
  def open_list_page(cls, numbers):
    request = cls.create_list_page_request(numbers)
    return urllib2.urlopen(request)

  @classmethod
  def get_list_page(cls, numbers):
    io = cls.open_list_page(numbers)
    page = io.read()
    io.close()
    return page
