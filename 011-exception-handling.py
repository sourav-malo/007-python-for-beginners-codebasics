x = input("Enter number x: ")
y = input("Enter number y: ")
# z = int(x) / int(y)
# it can occur exception 
# print(z) 

# exception handling
try:
  z = int(x) / int(y)
except Exception as e:
  print(type(e) . __name__)
  z = None
print(z)

# specific exception handling
try:
  z = int(x) / int(y)
except ZeroDivisionError as e:
  print(type(e) . __name__)
  z = None
print(z)