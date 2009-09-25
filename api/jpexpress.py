# -*- coding: utf-8 -*-

import json
from google.appengine.ext import webapp

from tracker.jpexpress.package.session import Session

class PackageListJson(webapp.RequestHandler):
  def get(self):
    param_numbers = self.request.get("numbers")
    array_numbers = param_numbers.split(",")

    session = Session()
    results = session.get_list_page(["144856020890"])

    result = {}

    """
    for record in results[u"一覧"]:
      number = record[u"送り状番号"]
      ret = {
      }
      result[number] = ret
    """

    """
    for number in array_numbers:
      ret = {
        "message": u"配達完了いたしました。",
        "current_state": u"配達完了いたしました。",
        "current_state_time": u"8/12 9:19",
        "type": u"ペリカン便",
        "detail": {
          "reception_date": "8/10",
          "delivery_time": u"8/12 午前中",
        },
      }
      result[number] = ret
    """

    output = {
      "success": True,
      "parameter": {
        "callback": None,
        "numbers": array_numbers,
      },
      "result": results.content,
    }

    #  u"送り状番号:リンク先"  
    #  u"送り状番号:パラメータ"
    #  u"最新状況"             
    #  u"最新状況:日時"        
    #  u"受付日"               
    #  u"お届け指定日"         
    #  u"扱区分"               

    #self.render_json(output)
    self.response.headers["Content-Type"] = "text/html"
    self.response.out.write(results.content)

  def render_json(self, body):
    self.response.headers["Content-Type"] = "text/javascript"
    self.response.out.write(json.write(body))
