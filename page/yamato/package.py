# -*- coding: utf-8 -*-

import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template

from tracker.yamato.package.tracking_number import TrackingNumber
from tracker.yamato.package.session import Session

class QueryPage(webapp.RequestHandler):
  def get(self):
    param_names   = ["num%02i" % (i + 1) for i in range(10)]
    number_params = [{"name": name, "value": self.request.get(name)} for name in param_names]
    numbers       = [param["value"] for param in number_params]

    results = []
    for number in numbers:
      if number == "":
        continue

      if TrackingNumber.is_valid(number):
        message = "正常"
      else:
        message = "不正な番号です"
      hash = {
        "number" : number,
        "message": message,
      }
      results.append(hash)

    values = {
      "results": results,
      "number_params": number_params,
    }
    path = os.path.join(os.path.dirname(__file__), "package_query.html")
    html = template.render(path, values)
    self.response.out.write(html)
