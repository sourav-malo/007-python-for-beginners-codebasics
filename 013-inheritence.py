class Vehicle:
  def getGeneralPurpose(self):
    print("It makes moving from one place to another easier")

class Car(Vehicle):
  def __init__(self, wheels, hasRoof):
    self.wheels = wheels
    self.hasRoof = hasRoof
  
  def getSpecialPurpose(self):
    self.getGeneralPurpose()
    print("It is mostly used for family tours")

class Motorcycle(Vehicle):
  def __init__(self, wheels, hasRoof):
    self.wheels = 2
    self.hasRoof = False 
  
  def getSpecialPurpose(self):
    self.getGeneralPurpose()
    print("It is mostly used for racing")

car1 = Car(4, True)
motorcycle1 = Motorcycle(2, False)

car1.getSpecialPurpose()
motorcycle1.getSpecialPurpose()