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

  @classmethod
  def trim_unwanted_tags(cls, html):
    result1 = cls.trim_script_tag(html)
    result2 = cls.trim_style_tag(result1)
    result3 = cls.trim_center_tag(result2)
    result4 = cls.trim_paragraph_tag(result3)
    result5 = cls.trim_bold_tag(result4)
    return result5

  @classmethod
  def trim_unwanted_nodes(cls, doc):
    # ヘッダを削除
    for i in range(4):
      doc.body.table.extract()
    doc.body.form.extract()
    for i in range(4):
      doc.body.table.extract()

    # フッタを削除
    doc.body.findAll("table", recursive = False)[-1].extract()

    # リンクを削除
    for elem in doc.body.findAll("a", {"name": re.compile(".+")}):
      elem.extract()
    for elem in doc.body.findAll("a", {"href": re.compile("^#")}):
      elem.extract()

    # ボタンを削除
    for elem in doc.body.findAll("div", {"class": "print_hide"}):
      elem.extract()

    # 水平線を削除
    for elem in doc.body.findAll("hr"):
      elem.extract()

    # 強制改行を削除
    for elem in doc.body.findAll("br"):
      elem.extract()

  @classmethod
  def create_doc(cls, html):
    src = cls.trim_unwanted_tags(html)
    doc = BeautifulSoup(src)
    cls.trim_unwanted_nodes(doc)
    return doc
