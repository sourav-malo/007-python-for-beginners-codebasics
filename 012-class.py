class Human:
  def __init__(self, name, occupation):
    self.name = name
    self.occupation = occupation

  def doWork(self): 
    if self.occupation == 'tennis player':
      print(self.name + " plays tennis!")
    elif self.occupation == 'cricketer':
      print(self.name + " plays cricket!")

human1 = Human('Roger Federer', 'tennis player')
human2 = Human('Virat Kohili', 'cricketer')

human1.doWork()
human2.doWork()