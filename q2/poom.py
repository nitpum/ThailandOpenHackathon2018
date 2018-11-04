import sys
import datetime
import operator

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

def addToDict(dict, key, value):
  if key not in dict:
    dict[key] = value
  else:
    dict[key] += value

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

# DO !!!

sorted_channels = sorted(channels.items(), key=operator.itemgetter(1), reverse=True)
for c in sorted_channels:
  print(c)

max = sorted_channels[0][1]

def filterMax(item):
  return item[1] == max
sorted_abc_channels = list(filter(filterMax, sorted_channels))
print("===============")
for c in sorted_abc_channels:
  print(c)
# sorted_channels = sorted(channels.items(), key=lambda kv: kv[1], reverse =False)
# sorted_a = sorted_channels.sort(key=operator.itemgetter(0))
# # for c in range(0, 5):
# #   channel = sorted_channels[len(sorted_channels) - 1 - c]
# #   sorted_a[channel[0]] = channel[1]
# #   print(channel[0] + " " + str(channel[1]))

# for c in range(5):
#   print(sorted_a[c])