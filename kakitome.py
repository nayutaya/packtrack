# -*- coding: utf-8 -*-

import urllib
import urllib2

base_params = {
  "SVID": "023",
  "locale": "ja",
  "searchKind": "S002",
  "reqCodeNo1": "00000000000",
  "reqCodeNo2": "",
  "reqCodeNo3": "",
  "reqCodeNo4": "",
  "reqCodeNo5": "",
  "reqCodeNo6": "",
  "reqCodeNo7": "",
  "reqCodeNo8": "",
  "reqCodeNo9": "",
  "reqCodeNo10": "",
}

params = base_params
query = urllib.urlencode(params)
url = "http://tracking.post.japanpost.jp/service/singleSearch.do" + "?" + query

print url
