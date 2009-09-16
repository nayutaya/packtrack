# -*- coding: utf-8 -*-

import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template

import page.yamato.package
import api.jpexpress

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
      (r"/yamato/package/query",      page.yamato.package.QueryPage),
      (r"/yamato/package/list\.json", page.yamato.package.ListJson),
      (r"/jpexpress/package/list\.json", api.jpexpress.PackageListJson),
    ],
    debug = True)
  run_wsgi_app(application)
