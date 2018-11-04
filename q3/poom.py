import sys
import datetime
import operator

# Variables
customers = []
companys = {}
campaigns = {}
campaignsUser = {}
average = {}

# Class
class Customer:
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

# Functions and Filters
# def addToDict(dict, key, value):
#   if key not in dict:
#     dict[key] = value
#   else:
#     dict[key] += value

# def filterObjectMax(max, i):
#   def filter(item):
#     return item[i] == max
#   return filter

# def filterCustomerPeriod(formDate, toDate):
#   def filter(customer):
#     return (formDate <= customer.time and customer.time >= toDate)
#   return filter

# def filterPeriod(formDate, toDate):
#   def filter(date):
#     return (formDate <= date and formDate >= toDate)
#   return filter


# Read Input
lines = sys.stdin.read().split('\n')
lineCount = 0
for line in lines:
  if (len(line.split('|')) >= 9 and line != "" and lineCount > 0):
    customer = Customer(line)
    # customers.append(customer)
    if customer.campaign not in  campaigns:
      campaigns[customer.campaign] = []
      campaigns[customer.campaign].append(0)
      campaigns[customer.campaign].append(0)
      campaigns[customer.campaign].append([])
    campaigns[customer.campaign][0] += 1
    if customer.id not in campaigns[customer.campaign][2]:
      campaigns[customer.campaign][1] += 1
      campaigns[customer.campaign][2].append(customer.id)
      

  lineCount += 1
# Sort
campaigns = sorted(campaigns.items(), key=lambda kv: kv[1], reverse =False)
# Print result
for c in range(len(campaigns)):
    campaign = campaigns[c][1]
    campaignName = campaigns[c][0]
    avg = campaign[0] / len(campaign[2])
    print(campaignName + " " + str("%.2f" % avg))