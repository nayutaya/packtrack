# -*- coding: utf-8 -*-

import re
from BeautifulSoup import BeautifulSoup

# 詳細ページ解析クラス
class DetailPageParser:
  def __init__(self):
    pass

  @classmethod
  def trim_script_tag(cls, html):
    pattern = re.compile(r"<script.+?>.+?</script>", re.IGNORECASE | re.DOTALL)
    return re.sub(pattern, "", html)

  @classmethod
  def trim_style_tag(cls, html):
    pattern = re.compile(r"<style.+?>.+?</style>", re.IGNORECASE | re.DOTALL)
    return re.sub(pattern, "", html)

  @classmethod
  def trim_center_tag(cls, html):
    pattern = re.compile(r"</?center>", re.IGNORECASE)
    return re.sub(pattern, "", html)

  @classmethod
  def trim_paragraph_tag(cls, html):
    pattern = re.compile(r"(?:<p.*?>|</p>)", re.IGNORECASE)
    return re.sub(pattern, "", html)

  @classmethod
  def trim_bold_tag(cls, html):
    pattern = re.compile(r"</?b>", re.IGNORECASE)
    return re.sub(pattern, "", html)
