# -*- coding: utf-8 -*-

import json
from google.appengine.ext import webapp

class PackageListJson(webapp.RequestHandler):
  def get(self):
    output = {
      "success": True,
    }

    self.response.headers["Content-Type"] = "text/javascript"
    self.response.out.write(json.write(output))
