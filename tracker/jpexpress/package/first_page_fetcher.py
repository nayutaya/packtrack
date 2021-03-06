# -*- coding: utf-8 -*-

import urllib
import urllib2

# 先頭ページ取得クラス
class FirstPageFetcher:
  def __init__(self, content):
    self.content = content

  @classmethod
  def create_url(cls):
    return "http://info.jpexpress.jp/confirm/confirmIndex.html"

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
    try:
      return io.read()
    finally:
      io.close()

  @classmethod
  def get(cls):
    return cls(cls.get_content())
