# -*- coding: utf-8 -*-

# 詳細ページクラス
class PackageDetailPage:
  def __init__(self):
    pass

  @classmethod
  def create_url(cls, jsession_id, params):
    return "http://info.jpexpress.jp/confirm/confirmDetail.html;jsessionid=" + jsession_id + "?" + params
