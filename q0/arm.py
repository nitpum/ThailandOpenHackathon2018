import sys
import datetime

class Customer:
  month = {
    ""
  }
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

customers = []

line = sys.stdin.readline()

""" read data """
while True:
  """ read line """
  line = sys.stdin.readline()
  if line != "":
    customers.append(Customer(line))
  else:
    break

def filterCustomer(id):
  def filter(customer):
    if(customer.id == id):
      return True
    else:
      return False
  return filter

filcus = list(filter(filterCustomer("150428059"), customers))
  
for cus in filcus:
  print(cus.type)

