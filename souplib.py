# -*- coding: utf-8 -*-

from BeautifulSoup import BeautifulSoup

def complement_no_value_attribute(soup, element_name, attr_name):
  elements = soup.findAll(element_name, {attr_name: None})
  for element in elements:
    for i in xrange(len(element.attrs)):
      if element.attrs[i] == (attr_name, None):
        element.attrs[i] = (attr_name, attr_name)
        break

def create_well_formed_html(html):
  soup = BeautifulSoup(html)
  complement_no_value_attribute(soup, "td", "nowrap")
  return soup.prettify()
