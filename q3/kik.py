import sys
import datetime

class Customer:
  month = {
    ""
  }
  def __init__(self, str):
    sep = str.strip().split('|')
    self.id = sep[0]
    self.timestamp = datetime.datetime.strptime(sep[1] + "|" + sep[2], '%d%b%Y|%H:%M:%S')
    self.cat = sep[3]
    self.subcat = sep[4]
    self.partner = sep[5]
    self.type = sep[6]
    self.campaign = sep[7]
    self.channel = sep[8]

customers = []
count={}
count_cus={}
count2={}
cus={}
line = sys.stdin.readline()
i = 0
max=0
""" read data """
while True:
  """ read line """
  line = sys.stdin.readline()
  if line != "":
    customers.append(Customer(line))
    if customers[i].campaign in count :
        count[customers[i].campaign]+=1
    else :
        count[customers[i].campaign]=1
    i+=1
  else:
    break


for customer in customers :
    if customer.id+customer.campaign not in count_cus :
        count_cus[customer.id+customer.campaign]=1
        if customer.campaign in count2 :
            count2[customer.campaign]+=1
        else :
            count2[customer.campaign]=1
for key in sorted(count2.keys()):
    temp=round(count[key]/count2[key],2)
    print(key,temp)
