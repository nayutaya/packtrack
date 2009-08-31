# -*- coding: utf-8 -*-

# 追跡セッションクラス
class PackageTrackingSession:
  def __init__(self):
    self.jsession_id = None

  def setup(self):
    if self.jsession_id is None:
      first_page = self.get_first_page()
      first_info = PackageFirstPageParser.parse(first_page.content)
      self.jsession_id = first_info["jsessionid"]
    return self

  def get_first_page(self):
    return PackageFirstPage.get()

  def get_list_page(self, numbers):
    self.setup()
    return PackageListPage.get(self.jsession_id, numbers)
