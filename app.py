# -*- coding: utf-8 -*-

import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template

class HomePage(webapp.RequestHandler):
  def get(self):
    values = {}
    path = os.path.join(os.path.dirname(__file__), "page/home.html")
    html = template.render(path, values)
    self.response.out.write(html)

if __name__ == "__main__":
  application = webapp.WSGIApplication(
    [
      (r"/", HomePage),
    ],
    debug = True)
  run_wsgi_app(application)
