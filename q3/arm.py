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

campaigns = {} 

for customer in customers:
  campaign = customer.campaign
  if campaign not in campaigns:
    campaigns[campaign] = {}

  if customer.id in campaigns[campaign]:
    campaigns[campaign][customer.id] += 1
  else:
    campaigns[campaign][customer.id] = 1

campaignStats = {}

for campaign in campaigns:
  for customer in campaigns[campaign]:
    if campaign not in campaignStats:
      campaignStats[campaign] = 0
    
    campaignStats[campaign] += campaigns[campaign][customer]

for campaign in campaignStats:
  avg = campaignStats[campaign] / len(campaigns[campaign])
  print(campaign + " " + str(round(avg,2)))
  