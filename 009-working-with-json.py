import json

# reading json files
file = open("C:\\Users\\soura\\Desktop\\007-python-for-beginners-codebasics\\files\\students.json", 'r')
studentsJson = file.read()
students = json.loads(studentsJson)
print(students["Salah"])
print(students["Sayem"])

# writing json files
students = {}
students["Salah"] =  {
  "name": "Salah",
  "address": "Amotola, Jumir Khan Sarak, Barishal - 8200",
  "age": 23
}
students["Sayem"] =  {
  "name": "Sayem",
  "address": "Rupatoli Housing, Barishal - 8200",
  "age": 20
}
studentsJson = json.dumps(students)
with open("C:\\Users\\soura\\Desktop\\007-python-for-beginners-codebasics\\files\\_students.json", 'w') as file:
  file.write(studentsJson)



