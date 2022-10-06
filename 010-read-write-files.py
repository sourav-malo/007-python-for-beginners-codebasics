# Write into a file
f = open("files/development.txt", 'w')
f.write("I love HTML\nI Love CSS\nI love JS\nI love PHP\nI love MySQL")
f.close()

# Append into a file
f = open("files/development.txt", "a")
f.write("\nI love React.js\nI love Node.js\nI love Express.js\nI love MongoDB")
f.close()

# Read a file line by line 
f = open("files/development.txt", "r")
for line in f:
  print(line)

# Read & Write Exercise
with open("files/development.txt", "r") as fRead, open("files/_development.txt", "w") as fWrite:
  for line in fRead:
    line = line.replace("\n", "")
    wordCount = len(line.split(" "))
    fWrite.write(line + " " + str(wordCount) + "\n")