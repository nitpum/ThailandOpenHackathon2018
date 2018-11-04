import sys
import datetime
import operator

# Class
class Customer:
  def __init__(self, str):
    sep = str.split('|')
    self.id = sep[0]
    self.timestamp = datetime.datetime.strptime(sep[1] + "|" + sep[2], '%d%b%Y|%H:%M:%S')
    self.cat = sep[3]
    self.subcat = sep[4]
    self.partner = sep[5]
    self.type = sep[6]
    self.campaign = sep[7]
    self.channel = sep[8]

# Variables
customers = []
lines = sys.stdin.read().split('\n')
lineCount = 0
data = 0
companys = {}
i = 0

# Read inputs
for line in lines:
  if (len(line.split('|')) >= 9 and line != "" and lineCount > 0):
    customers.append(Customer(line))
  lineCount += 1

# Counting company
for c in customers:
  if c.partner not in companys:
    companys[c.partner] = 0
  companys[c.partner] += 1

# Sorted by 
companys = sorted(companys.items(), key=lambda kv: kv[1])

# Print results
for c in range(0, 5):
  print (companys[len(companys) - 1 - c][0] + " " + str(companys[len(companys) - 1 - c][1]))