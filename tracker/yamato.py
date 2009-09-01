# -*- coding: utf-8 -*-



class PackageDetailPage:
  def __init__(self):
    pass


  @classmethod
  def open(cls, numbers):
    request = cls.create_request(numbers)
    return urllib2.urlopen(request)

  @classmethod
  def get_content(cls, numbers):
    io = cls.open(numbers)
    try:
      return io.read()
    finally:
      io.close()
