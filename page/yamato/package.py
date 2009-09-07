# -*- coding: utf-8 -*-

import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template

class QueryPage(webapp.RequestHandler):
  def get(self):
    param_names = ["num%02i" % (i + 1) for i in range(10)]
    numbers     = [self.request.get(name) for name in param_names]

    values = {}
    path = os.path.join(os.path.dirname(__file__), "package_query.html")
    html = template.render(path, values)
    self.response.out.write(html)
