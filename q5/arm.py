import sys
import datetime
import operator
from functools import reduce

class Customer:
  month = {
    ""
  }
  def __init__(self, str):
    sep = str.strip().split('|')
    self.id = sep[0]
    self.originaltime = sep[2]
    self.time = datetime.datetime.strptime(sep[1] + "|" + sep[2], '%d%b%Y|%H:%M:%S')
    self.daytime = datetime.datetime.strptime(sep[2], '%H:%M:%S')
    self.cat = sep[3].strip()
    self.subcat = sep[4].strip()
    self.partner = sep[5].strip()
    self.type = sep[6].strip()
    self.campaign = sep[7].strip()
    self.channel = sep[8].strip()
  def __str__(self):
    return "{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}".format(self.id, self.time, self.cat, self.subcat, self.partner, self.type, self.campaign, self.channel)

customers = []

""" read data """
line = sys.stdin.readline()

while True:
  """ read line """
  line = sys.stdin.readline()
  if line != "":
    customers.append(Customer(line))
  else:
    break

customers = list(sorted(customers, key=operator.attrgetter('daytime')))

def totalSec(time):
  return time.hour*60*60 + time.minute*60 + time.second

limitRange = 20*60
l = 0
r = 0

maxUse = 0
maxStat = []

while l < len(customers):
  if(r >= len(customers)):
    break

  timeDiff = totalSec(customers[r].time) - totalSec(customers[l].time)
  if(timeDiff < 0):
    break

  # print(timeDiff)
  if timeDiff < limitRange:
    r += 1
  else:
    l +=1
  
  if(r-l > maxUse):
    maxUse = r-l
    maxStat.clear()
  if(r-l == maxUse):
    maxStat.append([l, r])

for value in maxStat:
  print(customers[value[0]].originaltime, customers[value[1]-1].originaltime, maxUse)

# print('c', maxUse)
# print(len(maxStat))