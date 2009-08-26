# -*- coding: utf-8 -*-

import re
import urllib
import urllib2


class PackageFirstPage:
  def __init__(self):
    pass

  @classmethod
  def create_first_page_url(cls):
    return "http://info.jpexpress.jp/confirm/confirmIndex.html"

  @classmethod
  def create_first_page_request(cls):
    return urllib2.Request(
      url = cls.create_first_page_url())

  @classmethod
  def open_first_page(cls):
    request = cls.create_first_page_request()
    return urllib2.urlopen(request)

  @classmethod
  def get_session_id(cls, html):
    pattern = re.compile(r"jsessionid=([0-9A-Z]+\.[0-9A-Z]+_[0-9A-Z]+)")
    match   = pattern.search(html)
    if match is not None:
      return match.group(1)
    else:
      return None


class PackageListPage:
  def __init__(self):
    pass

  @classmethod
  def create_list_page_url(cls, session_id):
    return "http://info.jpexpress.jp/confirm/confirmIndex.html;jsessionid=" + session_id

  @classmethod
  def create_list_page_base_params(cls):
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
  def create_list_page_number_params(cls, numbers):
    params = {}
    for i, number in enumerate(numbers[:10]):
      params["includeChildBody:confirmIndexForm:denpyoNo%i" % i] = number
    return params

  @classmethod
  def create_list_page_params(cls, numbers):
    params = cls.create_list_page_base_params()
    params.update(cls.create_list_page_number_params(numbers))
    return params

  @classmethod
  def create_list_page_request(cls, session_id, numbers):
    params = cls. create_list_page_params(numbers)
    return urllib2.Request(
      url  = cls.create_list_page_url(session_id),
      data = urllib.urlencode(params))

  @classmethod
  def open_list_page(cls, session_id, numbers):
    request = cls.create_list_page_request(session_id, numbers)
    return urllib2.urlopen(request)

def create_detail_page_url(session_id, params):
  return "http://info.jpexpress.jp/confirm/confirmDetail.html;jsessionid=" + session_id + "?" + params
