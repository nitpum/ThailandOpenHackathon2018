import sys

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

# print(customers)

for c in customers:
  if (c.customer_id == '150428059'):
    print(c.redeem_type)