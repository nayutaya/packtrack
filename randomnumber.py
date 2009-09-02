# -*- coding: utf-8 -*-

from tracker import jppost

numbers = []
for i in range(10):
  number = jppost.PackageTrackingNumber.create_random_number("2497")
  numbers.append(number)

for number in numbers:
  print number
