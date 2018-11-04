import sys
import datetime
import operator

class Customer:
  month = {
    ""
  }
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

customers = []

""" read data """
line = sys.stdin.readline()

while True:
  """ read line """
  line = sys.stdin.readline()
  if line != "":
    customers.append(Customer(line))
  else:
    break

partner = {}

for customer in customers:
  if customer.partner in partner:
    partner[customer.partner] += 1
  else:
    partner[customer.partner] = 1

rank = sorted(partner.items(), key=operator.itemgetter(1), reverse=True)

for i in range(0,5):
  print(rank[i][0] + ' ' + str(rank[i][1]))