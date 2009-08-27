# -*- coding: utf-8 -*-

import re
from tracker import jpexpress

if False:
  page1 = jpexpress.PackageFirstPage.get()
  f = open("page1.html", "wb")
  f.write(page1.content)
  f.close()
else:
  f = open("page1.html", "rb")
  page1 = jpexpress.PackageFirstPage(f.read())
  f.close()

session_id = page1.get_jsession_id()
print session_id


numbers = ["348012244355", "348011824893", "348011053121"]
print numbers

if False:
  page2 = jpexpress.PackageListPage.get(session_id, numbers)
  f = open("page2.html", "wb")
  f.write(page2.content)
  f.close()
else:
  f = open("page2.html", "rb")
  page2 = jpexpress.PackageListPage(f.read())
  f.close()

"""
pattern = re.compile(r"href=\"confirmDetail\.html;.+?\?(.+?)\"")
for params in pattern.findall(page2.content):
  params2 = re.compile(r"&amp;").sub("&", params)
  print "---"
  print jpexpress.PackageDetailPage.create_url(session_id, params2)
"""


from BeautifulSoup import BeautifulSoup
soup = BeautifulSoup(page2.content)

def get_list_table(soup):
  div = soup.find("div", {"id": "isGetData"})
  return div.find("table")

list_table = get_list_table(soup)

#print list_table.prettify()

def get_list_rows(table):
  for i, row in enumerate(table.findAll("tr")):
    if i == 0: continue
    cells = row.findAll("td")
    print "----"
    print row.prettify()
    result_no_cell         = cells[0]
    tracking_number_cell   = cells[1]
    current_status_cell    = cells[2]
    accept_date_cell       = cells[3]
    arrival_date_cell      = cells[4]
    handling_division_cell = cells[5]
    mail_cell              = cells[6] # 用途不明
    #print ("recv_date", recv_date)
    #print ("send_date", send_date)
    #print ("division", division)
    #print ("mail", mail)
    hash = {
      u"No"                 : result_no_cell.center.span.string,
      u"送り状番号"         : tracking_number_cell.div.a.contents[0].strip(),
      u"送り状番号:リンク先": tracking_number_cell.div.a["href"],
      u"最新状況"           : current_status_cell.span.contents[0].strip(),
      u"最新状況:日時"      : current_status_cell.span.contents[2].strip(),
    }
    print hash
    #for k, v in hash.items():
    #  print "--"
    #  print k + u": " + v

get_list_rows(list_table)
