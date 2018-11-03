# List
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

# Access item
fruits[1]

# Change value
fruits[1] = "apple"

# Count element
fruits.count('apple')

# Find index
fruits.index('banana')
fruits.index('banana', 4)  # Find next banana starting a position 4

# Reverse list
fruits.reverse()

# Append
fruits.append('grape')

# Insert
fruits.insert(1, "orange")

# Remove
fruits.remove("orange")

# Delete
del fruits[1]

# Sort
fruits.sort()

# Sort with function
# A function that returns the length of the value:
def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(key=myFunc)

# Pop
fruits.pop()

# Clear
fruits.clear()

# Make list constructor
list2 = list(('apple', 'orange')) # note the double round-brackets
# ['apple', 'orange']

# Extend
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']

fruits.extend(cars) # ['apple', 'banana', 'cherry', 'Ford', 'BMW', 'Volvo']

# Copy
x = fruits.copy() # x = ['apple', 'banana', 'cherry']

# Loop through a list
for x in fruits:
  print(x)

# Check if item exists
if "apple" in fruits:
  print("Yes, apple is exists")

# List length
len(fruits)