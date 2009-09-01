# -*- coding: utf-8 -*-

from tracker.yamato.package.detail_page_fetcher import DetailPageFetcher

numbers = ["225303520584", "249790484403"]

page2 = DetailPageFetcher.get_content(numbers)

f = open("page2.html", "wb")
f.write(page2)
f.close()
print page2
