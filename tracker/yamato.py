# -*- coding: utf-8 -*-

import urllib
import urllib2


class PackageDetailPage:
  def __init__(self):
    pass

  @classmethod
  def create_detail_page_url(cls):
    return "http://toi.kuronekoyamato.co.jp/cgi-bin/tneko"

  @classmethod
  def create_detail_page_base_params(cls):
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

  @classmethod
  def create_detail_page_number_params(cls, numbers):
    params = {}
    for i, number in enumerate(numbers[:10]):
      params["number%02i" % (i + 1)] = number
    return params

  @classmethod
  def create_detail_page_params(cls, numbers):
    params = cls.create_detail_page_base_params()
    params.update(cls.create_detail_page_number_params(numbers))
    return params

  @classmethod
  def create_detail_page_request(cls, numbers):
    params = cls.create_detail_page_params(numbers)
    return urllib2.Request(
      url  = cls.create_detail_page_url(),
      data = urllib.urlencode(params))

  @classmethod
  def open_detail_page(cls, numbers):
    request = cls.create_detail_page_request(numbers)
    return urllib2.urlopen(request)

  @classmethod
  def get_detail_page(cls, numbers):
    io = cls.open_detail_page(numbers)
    page = io.read()
    io.close()
    return page
