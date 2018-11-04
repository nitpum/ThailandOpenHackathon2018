import sys
import datetime

# Class
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

# Variable
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
# Counting find max
for key in count:
    if count[key]>max :
        max=count[key]
        lis.clear()
        lis.append(key)
    elif count[key]==max :
        lis.append(key)
lis.sort(reverse=True)
# Print result
for str in lis:
    print(str)
