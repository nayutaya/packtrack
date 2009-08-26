# -*- coding: utf-8 -*-

from tracker import sagawa

numbers = [
  "600097281033",
  "600092368315"
]

fields = sagawa.get_first_page_params()
state = fields["jsf_state_64"]
tree  = fields["jsf_tree_64"]

params = sagawa.PackageDetailPage.create_params(state, tree, numbers)
#print params

result = sagawa.PackageDetailPage.get_content(params)
print result
