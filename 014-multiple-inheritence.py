class Father:
  def getSkills(self):
    print("programming")

class Mother:
  def getSkills(self):
    print("cooking")

class Child(Father, Mother):
  def getSkills(self):
    Father.getSkills(self)
    Mother.getSkills(self)
    print("sports")
  
child1 = Child()
child1.getSkills()

