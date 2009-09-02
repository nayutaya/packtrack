# -*- coding: utf-8 -*-

from tracker.yamato.package.session import Session
from tracker.yamato.package.list_page_fetcher import ListPageFetcher
from tracker.yamato.package.list_page_parser import ListPageParser


session = Session()
#print session.get_list(["225303520584", "249790484403"])

numbers = [
  "249724973934",
]

page = ListPageFetcher.get_content(numbers)
f = open("yamato.html", "wb")
f.write(page)
f.close()

info = ListPageParser.parse(page)
#print info

for item1 in info[u"一覧"]:
  for key1, value1 in item1.items():
    if isinstance(value1, basestring):
      print key1 + ": '" + value1 + "'"
    elif value1 is not None:
      print key1 + ":"
      for item2 in value1:
        for key2, value2 in item2.items():
          print "  " + key2 + ": '" + value2 + "'"
        print "  ---"
  print "---"
