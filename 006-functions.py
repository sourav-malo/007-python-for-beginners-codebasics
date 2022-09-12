def sum(a, b):
  return a + b

print(sum(5, 6))

# unordered arguments 
def sub(a, b):
  return a - b

print(sub(b = 5, a = 6))

# default arguments + documentation string
def div(a, b = 1):
  """ 
    This function takes two integer numbers as input and returns their division as an output
  """
  return a / b

print(div(6))