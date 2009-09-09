# -*- coding: utf-8 -*-

from BeautifulSoup import BeautifulSoup

# 初期ページ解析クラス
class FirstPageParser:
  @classmethod
  def parse(cls, content):
    hidden_fields = {}

    soup = BeautifulSoup(content)
    for field in soup.findAll("input", {"type": "hidden"}):
      field_name, field_value = None, None
      for (attr_name, attr_value) in field.attrs:
        if   attr_name == "name" : field_name  = attr_value
        elif attr_name == "value": field_value = attr_value
      hidden_fields[field_name] = field_value

    return {
      "jsf_state_64": hidden_fields["jsf_state_64"],
      "jsf_tree_64": hidden_fields["jsf_tree_64"],
    }
