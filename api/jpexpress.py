# -*- coding: utf-8 -*-

import json
from google.appengine.ext import webapp

class PackageListJson(webapp.RequestHandler):
  def get(self):
    output = {
      "success": True,
      "parameter": {
        "callback": None,
        "numbers": ["144856020890"],
      },
      "result": {
        "144856020890": {
          "message": u"配達完了いたしました。",
          "current_state": u"配達完了いたしました。",
          "current_state_time": u"8/12 9:19",
          "type": u"ペリカン便",
          "detail": {
            "reception_date": "8/10",
            "delivery_time": u"8/12 午前中",
          },
        },
      },
    }

    #u"一覧"
    #  u"No"                   
    #  u"送り状番号"           
    #  u"送り状番号:リンク先"  
    #  u"送り状番号:パラメータ"
    #  u"最新状況"             
    #  u"最新状況:日時"        
    #  u"受付日"               
    #  u"お届け指定日"         
    #  u"扱区分"               

    self.response.headers["Content-Type"] = "text/javascript"
    self.response.out.write(json.write(output))
