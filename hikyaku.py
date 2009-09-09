# -*- coding: utf-8 -*-

from tracker.sagawa.package.first_page_fetcher import FirstPageFetcher
from tracker.sagawa.package.first_page_parser import FirstPageParser
from tracker import sagawa_old

numbers = [
  "600097281033",
  "600092368315"
]

page = FirstPageFetcher.get()
data = FirstPageParser.parse(page.content)
state = data["jsf_state_64"]
tree  = data["jsf_tree_64"]
exit()

result = sagawa_old.PackageDetailPage.get_content(state, tree, numbers)
print result
