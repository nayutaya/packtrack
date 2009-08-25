# -*- coding: utf-8 -*-

import re
import urllib
import urllib2
from tracker import yamato

numbers = ["225303520584", "249790484403"]

io = yamato.open_detail_page(numbers)
page2 = io.read()
io.close()

f = open("page2.html", "wb")
f.write(page2)
f.close()

#print page2
