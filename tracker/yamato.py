# -*- coding: utf-8 -*-

import urllib
import urllib2


class PackageDetailPage:
  def __init__(self):
    pass

  @classmethod
  def create_url(cls):
    return "http://toi.kuronekoyamato.co.jp/cgi-bin/tneko"

  @classmethod
  def create_base_params(cls):
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
  def create_number_params(cls, numbers):
    params = {}
    for i, number in enumerate(numbers[:10]):
      params["number%02i" % (i + 1)] = number
    return params

  @classmethod
  def create_params(cls, numbers):
    params = cls.create_base_params()
    params.update(cls.create_number_params(numbers))
    return params

  @classmethod
  def create_request(cls, numbers):
    params = cls.create_params(numbers)
    return urllib2.Request(
      url  = cls.create_url(),
      data = urllib.urlencode(params))

  @classmethod
  def open(cls, numbers):
    request = cls.create_request(numbers)
    return urllib2.urlopen(request)

  @classmethod
  def get_content(cls, numbers):
    io = cls.open(numbers)
    page = io.read()
    io.close()
    return page
