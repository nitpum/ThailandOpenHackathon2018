import sys
import datetime
import operator

class Customer:
  month = {
    ""
  }
  def __init__(self, str):
    sep = str.strip().split('|')
    self.id = sep[0]
    self.time = datetime.datetime.strptime(sep[1] + "|" + sep[2], '%d%b%Y|%H:%M:%S')
    self.cat = sep[3]
    self.subcat = sep[4]
    self.partner = sep[5]
    self.type = sep[6]
    self.campaign = sep[7]
    self.channel = sep[8]
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

couple = {}

for customer in customers:
  pair = customer.channel + " " + customer.subcat
  if pair in couple:
    couple[pair] += 1
  else:
    couple[pair] = 1

rank = sorted(couple.items(), key=operator.itemgetter(1), reverse=True)

max = rank[0][1]

def filterMax(item):
  return item[1] == max

maxRank = list(filter(filterMax, rank))
maxRank.sort(key=operator.itemgetter(0))

for item in maxRank:
  print(item[0])