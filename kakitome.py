# -*- coding: utf-8 -*-

import urllib
import urllib2
import random
import time

def create_random_number(prefix = ""):
  number = prefix
  while len(number) < 11:
    number += str(random.randint(0, 9))
  return number

base_params = {
  "SVID": "023",
  "locale": "ja",
  "searchKind": "S002",
  "reqCodeNo1": "",
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

for i in range(50):
  number_params = {
    "reqCodeNo1": create_random_number(),
    "reqCodeNo2": create_random_number(),
    "reqCodeNo3": create_random_number(),
    "reqCodeNo4": create_random_number(),
    "reqCodeNo5": create_random_number(),
    "reqCodeNo6": create_random_number(),
    "reqCodeNo7": create_random_number(),
    "reqCodeNo8": create_random_number(),
    "reqCodeNo9": create_random_number(),
    "reqCodeNo10": create_random_number(),
  }

  params = base_params
  params.update(number_params)
  print params

  query = urllib.urlencode(params)
  url = "http://tracking.post.japanpost.jp/service/singleSearch.do" + "?" + query
  print url

  io = urllib2.urlopen(url)
  page = io.read()
  io.close()

  fname = "test/%03i.html" % i
  print fname

  f = open(fname, "wb")
  f.write(page)
  f.close()

  time.sleep(0.5)
