import re # Use for regex

# String concat
'a' + 'b' # ab

# String repeated
'a' * 3 # aaa

# String concat with int
'a' + str(3) # a3

'{0} is {1}'.format('name', 'lastname')

'A'.lower()
'a'.upper()

m = re.match('A', 'ABC')
print(m.group(0))

print('Art: %5d, Price per Unit: %8.2f' % (435, 59.058))