import sys
import datetime
import operator

# Variable
customers = []
companys = {}

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

# Functions
def addToDict(dict, key, value):
  if key not in dict:
    dict[key] = value
  else:
    dict[key] += value

def filterObjectMax(max, i):
  def filter(item):
    return item[i] == max
  return filter

def filterCustomerPeriod(formDate, toDate):
  def filter(customer):
    return (formDate <= customer.time and customer.time >= toDate)
  return filter

def filterPeriod(formDate, toDate):
  def filter(date):
    return (formDate <= date and formDate >= toDate)
  return filter
  
# Read Input
lines = sys.stdin.read().split('\n')
lineCount = 0
for line in lines:
  if (len(line.split('|')) >= 9 and line != "" and lineCount > 0):
    customer = Customer(line)
    customers.append(customer)
  lineCount += 1