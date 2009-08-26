# -*- coding: utf-8 -*-

from tracker import sagawa

numbers = [
  "600097281033",
  "600092368315"
]

#print sagawa.get_first_page()

params = sagawa.get_first_page_params()
params.update(sagawa.create_detail_page_number_params(numbers))
#print params

result = sagawa.get_detail_page(params)
print result
