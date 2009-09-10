# -*- coding: utf-8 -*-

import re
import random

# 追跡番号クラス
class TrackingNumber:
  pattern = re.compile(r"^[0-9]{12}$")

  def __init__(self):
    pass

  @classmethod
  def create_check_digit(cls, body_digits):
    return str(int(body_digits) % 7)

  @classmethod
  def split_check_digit(cls, digits):
    return (digits[0:11], digits[11:12])

  @classmethod
  def is_valid(cls, digits):
    if cls.pattern.match(digits) is None: return False
    body_digits, check_digit = cls.split_check_digit(digits)
    if check_digit != cls.create_check_digit(body_digits): return False
    return True

  @classmethod
  def create_random_number(cls, prefix = ""):
    number = prefix
    while len(number) < 11:
      number += str(random.randint(0, 9))
    return number + cls.create_check_digit(number)
