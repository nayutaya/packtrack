# -*- coding: utf-8 -*-

from first_page import FirstPage
from first_page_parser import FirstPageParser
from list_page import ListPage

# セッションクラス
class Session:
  def __init__(self):
    self.jsession_id = None

  def setup(self):
    if self.jsession_id is None:
      first_page = self.get_first_page()
      first_info = FirstPageParser.parse(first_page.content)
      self.jsession_id = first_info["jsessionid"]
    return self

  def get_first_page(self):
    return FirstPage.get()

  def get_list_page(self, numbers):
    self.setup()
    return ListPage.get(self.jsession_id, numbers)
