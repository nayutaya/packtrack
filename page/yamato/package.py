# -*- coding: utf-8 -*-

import os
import re
import json
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

    valid_numbers = [number for number in numbers if TrackingNumber.is_valid(number)]
    session = Session()
    list    = session.get_list(valid_numbers)

    table = {}
    for record in list[u"一覧"]:
      tracking_number = re.sub("-", "", record[u"伝票番号"])
      message         = unicode(record[u"メッセージ"])
      table[tracking_number] = {
        "message": message,
      }

    results = []
    for number in numbers:
      if number == "":
        continue

      if TrackingNumber.is_valid(number):
        record = table.get(number)
        if record is not None:
          message = record["message"]
        else:
          message = "情報なし"
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

import api
class ListJson(webapp.RequestHandler):
  def get(self):
    params  = api.ListParameter(self.request)
    session = Session()
    data    = session.get_list(params.numbers)

    result = api.ListConverter.convert(data)

    output = {
      "success": True,
      "parameter": {
        "callback": None,
        "numbers" : params.numbers,
      },
      "result": result,
    }

    self.response.headers["Content-Type"] = "text/javascript"
    self.response.out.write(json.write(output))
