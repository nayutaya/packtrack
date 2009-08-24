# -*- coding: utf-8 -*-

import re
import logging
import urllib
from google.appengine.api import urlfetch

from tracker import sagawa


#print "Content-Type: text/plain"
print "Content-Type: text/html"
print ""

numbers = [
  "600097281033",
  "600092368315"
]

params = sagawa.get_first_page_params()
params.update(sagawa.create_detail_page_number_params(numbers))
#print params

result = sagawa.fetch_detail_page(params)
#print result.status_code
print result.content
