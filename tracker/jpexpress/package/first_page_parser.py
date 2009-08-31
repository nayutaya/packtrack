# -*- coding: utf-8 -*-

import re

# 先頭ページ解析クラス
class PackageFirstPageParser:
  @classmethod
  def parse(cls, src):
    return {
      "jsessionid": cls.get_jsession_id(src),
    }

  @classmethod
  def get_jsession_id(cls, src):
    pattern = re.compile(r"jsessionid=([0-9A-Z]+\.[0-9A-Z]+_[0-9A-Z]+)")
    match   = pattern.search(src)
    return match.group(1) if match is not None else None
