for i in range(2, 5):
  print(i)

# summation of even numbers (two approaches)
evens = [2, 4, 6, 8, 10]
total = 0

for item in evens:
  total += item 
print(total)

total = 0
for i in range(len(evens)):
  total += evens[i]
print(total)

# summation of sorted nums less than 5 (using break)
nums = [2, 4, 5, 6, 7, 8, 9, 10]
total = 0
for item in nums:
  if(item >= 5):
    break 
  total += item 
print(total)

# summation of sorted nums even (using continue)
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 0
for item in nums:
  if(item % 2 == 1):
    continue
  total += item 
print(total)