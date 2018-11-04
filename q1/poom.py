import sys
import operator

class customer:
  def __init__(self, line):
    self.customer_id, self.redemp_dt, self.redemp_tm, self.cat_desc, self.sub_cat_desc, self.prntr_desc, self.redeem_type, self.campaign, self.channel = line.split('|')    
  def __str__(self):
    return self.customer_id

customers = []

lines = sys.stdin.read().split('\n')
lineCount = 0
data = 0

for line in lines:
  if (len(line.split('|')) >= 9 and line != "" and lineCount > 0):
    customers.append(customer(line))
  lineCount += 1

company = {}

for c in customers:
  if c.prntr_desc in company:
    pass
  else:
    company[c.prntr_desc] = 0
  company[c.prntr_desc] += 1

i = 0
# ASc
# sorted_company = sorted(company.items(), key=lambda kv: kv[1])
# DESC
sorted_company = sorted(company.items(), key=lambda kv: kv[1], reverse =True)
for c in range(0, 5):
  print (sorted_company[len(sorted_company) - 1 - c][0] + " " + str(sorted_company[len(sorted_company) - 1 - c][1]))