# -*- coding: utf-8 -*-

from tracker import sagawa

numbers = [
  "600097281033",
  "600092368315"
]

page = sagawa.PackageFirstPage.get()

state = page.get_jsfstate()
tree  = page.get_jsftree()

result = sagawa.PackageDetailPage.get_content(state, tree, numbers)
print result
