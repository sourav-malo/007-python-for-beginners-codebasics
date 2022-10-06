class Accident(Exception):
  def __init__(self, msg):
    self.msg = msg 
  
  def getMessage(self):
    return self.msg

try:
  raise Accident('accident occurs')
except Accident as e:
  print(e)