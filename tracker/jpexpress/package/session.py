# -*- coding: utf-8 -*-

from first_page_fetcher import FirstPageFetcher
from first_page_parser import FirstPageParser
from list_page_fetcher import ListPageFetcher
from list_page_parser import ListPageParser
from detail_page_fetcher import DetailPageFetcher
from detail_page_parser import DetailPageParser

# セッションクラス
class Session:
  def __init__(self):
    self.jsession_id = None

  def setup(self):
    if self.jsession_id is None:
      first = self.get_first()
      self.jsession_id = first["jsessionid"]
    return self

  def get_first_page(self):
    return FirstPageFetcher.get()

  def get_first(self):
    page = self.get_first_page()
    return FirstPageParser.parse(page.content)

  def get_list_page(self, numbers):
    self.setup()
    return ListPageFetcher.get(self.jsession_id, numbers)

  def get_list(self, numbers):
    page = self.get_list_page(numbers)
    return ListPageParser.parse(page.content)

  def get_detail_page(self, params):
    self.setup()
    return DetailPageFetcher.get(self.jsession_id, params)

  def get_detail(self, params):
    page = self.get_detail_page(params)
    return DetailPageParser.parse(page.content)
