import sys
import datetime
import operator

# Variables
customers = []
timetable = []

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

# def filterTimePeriod(formTime, toDate):
#   def filter

for i in range(1441):
  timetable.append([0,61,-1])

# Read Input
lines = sys.stdin.read().split('\n')
lineCount = 0
for line in lines:
  if (len(line.split('|')) >= 9 and line != "" and lineCount > 0):
    customer = Customer(line)
    customers.append(customer)
    value = customer.time.hour * 60 + customer.time.minute
    # if value not in timetable:
    #   timetable[value] = [0,0,0]
    timetable[value][0] += 1
    if timetable[value][1] > customer.time.second:
      timetable[value][1] = customer.time.second
    if timetable[value][2] < customer.time.second:
      timetable[value][2] = customer.time.second
  lineCount += 1

for i in range(1, len(timetable)):
  # print(i)
  timetable[i][0] = timetable[i][0] + timetable[i - 1][0]  

maxValue = timetable[20][0]
for i in range(21, len(timetable)):
  if timetable[i][0]-timetable[i-20-1][0] > maxValue:
    maxValue = timetable[i][0]-timetable[i-20-1][0]

maxCell = []
for i in range(21, len(timetable)):
  if timetable[i][0]-timetable[i-20-1][0] == maxValue:
    maxCell.append(i)

def toTime(timeValue):
  hour = 0
  while timeValue >= 60:
    hour += 1
    timeValue /= 60
  return str(hour) + ":" + str("%.0f" % timeValue)
  
for c in maxCell:
  print(str(timetable[c - 20][1]) + " "  + str(timetable[c][2]))
  print(toTime(c - 200) + " "  + toTime(c))
