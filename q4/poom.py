import sys
import datetime
import operator

# Variables
customers = []
companys = {}
campaigns = {}
campaignsUser = {}
average = {}
n = 0
k = 0

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
  def __lt__(self, other):
    return self.time < other.time

# Functions and Filters
def amazonFilter(customer):
  return (customer.partner == "Cafe Amazon")

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
    customers.append(customer)
  lineCount += 1

# Sort date then sort id
customers.sort()
customers.sort(key=operator.attrgetter('id'))
# Counting
for i in range(len(customers) - 1):
  if customers[i].id == customers[i + 1].id:
    if customers[i].partner == "Cafe Amazon":
      n += 1
    if customers[i].partner == "Cafe Amazon" and customers[i + 1].cat == "Dining":
      k += 1

# Print results
p =  k / n
print("%.2f" % p)
