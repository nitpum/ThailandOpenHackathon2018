import sys
import datetime

# Class
class Customer:
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

# Variables
customers = []
count={}
line = sys.stdin.readline()
i = 0

""" read data """
while True:
  """ read line """
  line = sys.stdin.readline()
  if line != "":
    customers.append(Customer(line))
    # Counting company
    if customers[i].partner + " " +customers[i].channel in count :
        count[customers[i].partner + " " + customers[i].channel]+=1
    else :
        count[customers[i].partner + " " + customers[i].channel]=1
    i+=1
  else:
    break

# Print results
for key in sorted(count.values):
    print(key)

