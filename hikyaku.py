# -*- coding: utf-8 -*-

from tracker.sagawa.package.first_page_fetcher import FirstPageFetcher
from tracker import sagawa_old

numbers = [
  "600097281033",
  "600092368315"
]

page = FirstPageFetcher.get()
print page
print page.content
exit()

page = sagawa_old.PackageFirstPage.get()

state = page.get_jsfstate()
tree  = page.get_jsftree()

result = sagawa_old.PackageDetailPage.get_content(state, tree, numbers)
print result
