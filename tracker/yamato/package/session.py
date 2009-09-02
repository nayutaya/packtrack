# -*- coding: utf-8 -*-

from detail_page_fetcher import DetailPageFetcher
from detail_page_parser import DetailPageParser

# セッションクラス
class Session:
  def __init__(self):
    pass

  def get_detail_page(self, numbers):
    return DetailPageFetcher.get(numbers)

  def get_detail(self, numbers):
    page = self.get_detail_page(numbers)
    return DetailPageParser.parse(page.content)
