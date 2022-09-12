odds = [1, 3, 5]
evens = [2, 4, 6]
primes = [2, 3, 5]

num = input("Enter a number: ")
num = int(num)

if num in odds and num in primes: 
  print(num, "is both an odd and prime number")
elif num in evens and num in primes: 
  print(num, "is both an even and prime number")
elif num in odds: 
  print(num, "is an odd number")
elif num in evens: 
  print(num, "is an even number")
elif num in primes: 
  print(num, "is a prime number")
else: 
  print("I don't actually the type of this number, sorry 😥")