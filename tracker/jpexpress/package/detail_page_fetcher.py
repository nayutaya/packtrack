# -*- coding: utf-8 -*-

import urllib
import urllib2

# 詳細ページ取得クラス
class DetailPageFetcher:
  def __init__(self, content):
    self.content = content

  @classmethod
  def create_base_url(cls):
    return "http://info.jpexpress.jp/confirm/confirmDetail.html"

  @classmethod
  def create_url(cls, jsession_id, params):
    return cls.create_base_url() + ";jsessionid=" + jsession_id + "?" + params

  @classmethod
  def create_request(cls, jsession_id, params):
    return urllib2.Request(
      url  = cls.create_url(jsession_id, params))

  @classmethod
  def open(cls, jsession_id, params):
    request = cls.create_request(jsession_id, params)
    return urllib2.urlopen(request)

  @classmethod
  def get_content(cls, jsession_id, params):
    io = cls.open(jsession_id, params)
    try:
      return io.read()
    finally:
      io.close()

  @classmethod
  def get(cls, jsession_id, params):
    return cls(cls.get_content(jsession_id, params))
