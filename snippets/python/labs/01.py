import csv 

class timstamp:
  def __init__(self, year, month, date, hour, mins, sec):
    self.year = year
    self.month = month
    self.date = date
    self.hour = hour
    self.min = mins
    self.sec = sec

class customer:
  def __init__(self, caller, promo, ans, timstamp):
    self.caller = caller
    self.promo = promo
    self.ans = ans
    self.timestamp = timstamp

customers = []

with open('../data.csv') as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=',')
  line_count = 0
  for row in csv_reader:
      customers.append(customer(row[0], row[1], row[2], row[3]))
  print(f'Processed {line_count} lines.')