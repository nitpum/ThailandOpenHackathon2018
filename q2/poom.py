import sys
import datetime


# List
customers = []
companys = {}

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



# def addCompany(company):
#   if company not in companys:
#     companys[company] = 0
#   else
#     companys[companys] += 1

channels = {}
subs = {}



# Read Input
lines = sys.stdin.read().split('\n')
lineCount = 0
for line in lines:
  if (len(line.split('|')) >= 9 and line != "" and lineCount > 0):
    customer = Customer(line)
    customers.append(customer)
    if customer.channel + " " + customer.subcat  not in channels:
      channels[customer.channel + " " + customer.subcat] = 0
    else:
      channels[customer.channel + " " + customer.subcat] += 1
    # if customer.channel not in channels:
    #   channels[customer.channel] = 0
    # else :
    #   channels[customer.channel] += 1
    # if customer.channel not in subs:
    #   channels[customer.subcat] = 0
    # else :
    #   channels[customer.subcat] += 1
  lineCount += 1

def addToDict(dict, key, value, defaultValue):
  if key not in dict:
    dict[key] = defaultValue
  else:
    dict[key] += value


sorted_company = sorted(channels.items(), key=lambda kv: kv[1], reverse =False)
# sorted_company = sorted(channels.items(), key=lambda(k, v): (-v, k))
# sorted_company = sorted(channels.items(), key=lambda(k, v): (-v, k))
# for v in sorted(channels.iteritems(), key=lambda(k, v): (-v, k)):
  # pass
sorted_a = {}
sorted_b = {}
for c in range(0, 5):
  # if sorted_company[len(sorted_company) - 1 - c][0] + " " + str(sorted_company[len(sorted_company) - 1 - c][1]) not in sorted_a
  sorted_a[sorted_company[len(sorted_company) - 1 - c][0]] =  sorted_company[len(sorted_company) - 1 - c][1]



  print (sorted_company[len(sorted_company) - 1 - c][0] + " " + str(sorted_company[len(sorted_company) - 1 - c][1]))