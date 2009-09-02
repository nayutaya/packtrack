# -*- coding: utf-8 -*-

from list_page_fetcher import ListPageFetcher
from list_page_parser import ListPageParser

# セッションクラス
class Session:
  def __init__(self):
    pass

  def get_list_page(self, numbers):
    return ListPageFetcher.get(numbers)

  def get_list(self, numbers):
    page = self.get_list_page(numbers)
    return ListPageParser.parse(page.content)
