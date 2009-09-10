# -*- coding: utf-8 -*-

from list_page_fetcher import ListPageFetcher

# セッションクラス
class Session:
  def __init__(self):
    pass

  def get_list_page(self, numbers):
    return ListPageFetcher.get(numbers)
