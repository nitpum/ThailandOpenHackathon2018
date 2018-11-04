import sys
import datetime
import operator

# Class
class Customer:
  def __init__(self, str):
    sp = str.split('|')
    sep = str.split('|')
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

# Variable
customers = []
companys = {}

# Functions and filter
def addToDict(dict, key, value):
  if key not in dict:
    dict[key] = value
  else:
    dict[key] += value

def filterMax(item):
  def filter(max):
    return item[1] == max
  return filter

channels = {}
subs = {}

# Read Input
lines = sys.stdin.read().split('\n')
lineCount = 0
for line in lines:
  if (len(line.split('|')) >= 9 and line != "" and lineCount > 0):
    customer = Customer(line)
    customers.append(customer)
    addToDict(channels, customer.channel + " " + customer.subcat, 1)
  lineCount += 1

# Sorted channels
channels = sorted(channels.items(), key=operator.itemgetter(1), reverse=True)
# Get max value
max = channels[0][1]
# Get all channel that aresame value as max
channels = list(filter(filterMax, channels))
channels.sort(key=operator.itemgetter(0))
# Print result
for c in channels:
  print(c[0])