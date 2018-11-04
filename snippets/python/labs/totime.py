fullDateSample = "2017-10-01 00:00:13"
dateSample = '2017-10-01'
timeSample = '00:00:13'

class date: 
  def __init__ (self, value):
    self.year, self.month, self.day = value.split('-')
  def __str__ (self):
    return '{0}-{1}-{2}'.format(self.year, self.month, self.day)

class time:
  def __init__ (self, data):
    self.hour, self.minute, self.sec = data.split(':')

class timestamp:
  def __init__ (self, data):
    d, t = data.split(' ')
    self.date = date(d)
    self.time = time(t)
  def __str__ (self):
    return '{0}-{1}-{2} {3}:{4}:{5}'.format(self.date.year, self.date.month, self.date.day, self.time.hour, self.time.minute, self.time.sec)

one = date(dateSample)
print(one)

two = timestamp(fullDateSample)
print(two)