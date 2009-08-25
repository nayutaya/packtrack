# -*- coding: utf-8 -*-

import urllib
import urllib2
import random
import re


class PackageTrackingNumber:
  def __init__(self):
    pass

  @classmethod
  def create_check_digit(cls, number):
    num = int(number)
    return str(num % 7)

  @classmethod
  def create_random_number(cls, prefix = ""):
    number = prefix
    while len(number) < 11:
      number += str(random.randint(0, 9))
    return number + cls.create_check_digit(number)


class PackageListPage:
  def __init__(self, content):
    self.content = content

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
  def create_params(cls, numbers):
    params = cls.create_base_params()
    params.update(cls.create_number_params(numbers))
    return params

  @classmethod
  def create_base_url(cls):
    return "http://tracking.post.japanpost.jp/service/singleSearch.do"

  @classmethod
  def create_url(cls, numbers):
    base   = cls.create_base_url()
    params = cls.create_params(numbers)
    return base + "?" + urllib.urlencode(params)

  @classmethod
  def create_request(cls, numbers):
    return urllib2.Request(
      url = cls.create_url(numbers))

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

  def get_body(self):
    pattern = re.compile(r"<body.*?>(.*)</body>", re.IGNORECASE | re.MULTILINE | re.DOTALL)
    match   = pattern.search(self.content)
    return match.group(1) if match is not None else ""
