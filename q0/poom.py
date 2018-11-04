import sys
import datetime

# Class
class Customer:
  def __init__(self, str):
    sep = str.split('|')
    self.id = sep[0]
    self.time = datetime.datetime.strptime(sep[1] + "|" + sep[2], '%d%b%Y|%H:%M:%S')
    self.cat = sep[3]
    self.subcat = sep[4]
    self.partner = sep[5]
    self.type = sep[6]
    self.campaign = sep[7]
    self.channel = sep[8]

# Variable
customers = []
lines = sys.stdin.read().split('\n')
lineCount = 0

# Read inputs
for line in lines:
  if (len(line.split('|')) >= 9 and line != "" and lineCount > 0):
    customers.append(Customer(line)) # Add customer to list
  lineCount += 1

# Print results
for c in customers:
  if (c.customer_id == '150428059'):
    print(c.redeem_type)