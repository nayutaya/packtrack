# -*- coding: utf-8 -*-

from first_page_fetcher import FirstPageFetcher
from first_page_parser import FirstPageParser
from list_page_fetcher import ListPageFetcher

# セッションクラス
class Session:
  def __init__(self):
    self.state = None
    self.tree  = None

  def get_first_page(self):
    return FirstPageFetcher.get()

  def get_list_page(self, numbers):
    self.setup()
    return ListPageFetcher.get(self.state, self.tree, numbers)

  def setup(self):
    if self.state is None:
      page       = self.get_first_page()
      data       = FirstPageParser.parse(page.content)
      self.state = data["jsf_state_64"]
      self.tree  = data["jsf_tree_64"]
    return self
