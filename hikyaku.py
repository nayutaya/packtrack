# -*- coding: utf-8 -*-

from tracker import sagawa

from BeautifulSoup import BeautifulSoup

numbers = [
  "600097281033",
  "600092368315"
]

page = sagawa.PackageFirstPage.get()

state = page.get_jsfstate()
tree  = page.get_jsftree()

params = sagawa.PackageDetailPage.create_params(state, tree, numbers)
#print params

result = sagawa.PackageDetailPage.get_content(params)
print result
