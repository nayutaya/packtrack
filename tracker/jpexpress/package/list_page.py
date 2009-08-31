# -*- coding: utf-8 -*-

import urllib
import urllib2

# 一覧ページクラス
class ListPage:
  def __init__(self, content):
    self.content = content

  @classmethod
  def create_url(cls, jsession_id):
    return "http://info.jpexpress.jp/confirm/confirmIndex.html;jsessionid=" + jsession_id

  @classmethod
  def create_base_params(cls):
    return {
      "includeChildBody:confirmIndexForm:doConfirmCareerList": "",
      "includeChildBody:confirmIndexForm/confirm/confirmIndex.html": "includeChildBody:confirmIndexForm",
      "includeChildBody:confirmIndexForm:denpyoNo0": "",
      "includeChildBody:confirmIndexForm:denpyoNo1": "",
      "includeChildBody:confirmIndexForm:denpyoNo2": "",
      "includeChildBody:confirmIndexForm:denpyoNo3": "",
      "includeChildBody:confirmIndexForm:denpyoNo4": "",
      "includeChildBody:confirmIndexForm:denpyoNo5": "",
      "includeChildBody:confirmIndexForm:denpyoNo6": "",
      "includeChildBody:confirmIndexForm:denpyoNo7": "",
      "includeChildBody:confirmIndexForm:denpyoNo8": "",
      "includeChildBody:confirmIndexForm:denpyoNo9": "",
    }

  @classmethod
  def create_number_params(cls, numbers):
    params = {}
    for i, number in enumerate(numbers[:10]):
      params["includeChildBody:confirmIndexForm:denpyoNo%i" % i] = number
    return params

  @classmethod
  def create_params(cls, numbers):
    params = cls.create_base_params()
    params.update(cls.create_number_params(numbers))
    return params

  @classmethod
  def create_request(cls, jsession_id, numbers):
    params = cls. create_params(numbers)
    return urllib2.Request(
      url  = cls.create_url(jsession_id),
      data = urllib.urlencode(params))

  @classmethod
  def open(cls, jsession_id, numbers):
    request = cls.create_request(jsession_id, numbers)
    return urllib2.urlopen(request)

  @classmethod
  def get_content(cls, jsession_id, numbers):
    io = cls.open(jsession_id, numbers)
    try:
      return io.read()
    finally:
      io.close()

  @classmethod
  def get(cls, jsession_id, numbers):
    return cls(cls.get_content(jsession_id, numbers))
