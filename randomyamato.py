# -*- coding: utf-8 -*-

from tracker import jppost

numbers = []
for i in range(10):
  number = jppost.PackageTrackingNumber.create_random_number("225")
  numbers.append(number)

for number in numbers:
  print number

from tracker.yamato.package.detail_page_fetcher import DetailPageFetcher

detail_page = DetailPageFetcher.get_content(numbers)
f = open("yamato.html", "wb")
f.write(detail_page)
f.close()
