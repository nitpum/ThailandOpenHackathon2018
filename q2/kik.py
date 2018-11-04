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
lis=[]
line = sys.stdin.readline()
i = 0
max=0
""" read data """
while True:
  """ read line """
  line = sys.stdin.readline()
  if line != "":
    customers.append(Customer(line))
    if customers[i].channel + " " + customers[i].subcat in count :
        count[customers[i].channel + " " + customers[i].subcat]+=1
    else :
        count[customers[i].channel + " " + customers[i].subcat]=1
    i+=1
  else:
    break
for key in count:
    if count[key]>max :
        max=count[key]
        lis.clear()
        lis.append(key)
    elif count[key]==max :
        lis.append(key)
lis.sort(reverse=True)
for str in lis:
    print(str)
