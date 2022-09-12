person = { "Salah": 23, "Aisha": 24, "Safiyyah": 1}
print(person)

person["Purnima"] = 33
print(person["Purnima"])

del person["Purnima"]
print(person)

for key in person:
  print(key, person[key])

for key, value in person.items(): 
  print(key, value)

print("Purnima" in person)
print("Aisha" in person)

person.clear()
print(person)

coordinates = (2, 3) # tuples are immutable
print(coordinates[0], coordinates[1])
