# -*- coding: utf-8 -*-

import re
import urllib
import urllib2
from tracker import yamato

io = yamato.open_detail_page()
page2 = io.read()
io.close()

f = open("page2.html", "wb")
f.write(page2)
f.close()

#print page2
