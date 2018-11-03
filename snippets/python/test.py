import csv

class data:
  def __init__(self, number, uid, des, date1, date2):
    self.number = number
    self.uid = uid
    self.des = des
    self.date1 = date1
    self.date2 = date2
  def __str__(self): # Call when print()
    return str(self.number) + " " + str(self.uid)

listData = []

for i in range(0, 10):
  listData.append(data(i, 123, 456, 789, 10))

for i in listData:
  print(i)

class Animal ():
  def __init__(self, name):
    self.name = name
  def __str__(self):
    return '{0} is {1}'.format(self.name, 'Animal')
  
class Chicken(Animal):
  pass

print(Chicken('hi'))