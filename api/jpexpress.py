# -*- coding: utf-8 -*-

from google.appengine.ext import webapp

class PackageListJson(webapp.RequestHandler):
  def get(self):
    self.response.headers["Content-Type"] = "text/javascript"
    pass
