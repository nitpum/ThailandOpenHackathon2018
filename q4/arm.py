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
    self.time = datetime.datetime.strptime(sep[1] + "|" + sep[2], '%d%b%Y|%H:%M:%S')
    self.cat = sep[3].strip()
    self.subcat = sep[4].strip()
    self.partner = sep[5].strip()
    self.type = sep[6].strip()
    self.campaign = sep[7].strip()
    self.channel = sep[8].strip()
  def __str__(self):
    return "{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}".format(self.id, self.time, self.cat, self.subcat, self.partner, self.type, self.campaign, self.channel)

customers = []

# Functions
def addToDict(dict, key, value):
  if key not in dict:
    dict[key] = value
  else:
    dict[key] += value


""" read data """
line = sys.stdin.readline()

while True:
  """ read line """
  line = sys.stdin.readline()
  if line != "":
    customers.append(Customer(line))
  else:
    break

n = 0
k = 0
stats = {}

# customers = list(sorted(customers, key=operator.attrgetter('time')))

for customer in customers:
  if customer.id not in stats:
    stats[customer.id] = 0
  
  # if 1 => amazon
  if stats[customer.id] == 1:
    if customer.cat == 'Dining':
      k += 1
    n += 1
    stats[customer.id] = 0
  else:
    if customer.partner == 'Cafe Amazon':
      stats[customer.id] = 1

print("{0:.2f}".format(k/n))