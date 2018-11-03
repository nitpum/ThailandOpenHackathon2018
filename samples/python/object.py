# Empty class
class Tree:
  pass

# Create object
Oak = Tree()

# Class with init function
class Car:
  def __init__(self, name, speed) # Every function in class, first paremeter is a instance of object
    self.name = name
    slef.speed = speed
  def myFunc(abc) # instance can be 
    print(abc.name)

testla = Car("Testla Car", 150)
testla.myFunc()
testla.speed = 200

# Delete Object Properties
del testla.speed

# Delete object
del testla