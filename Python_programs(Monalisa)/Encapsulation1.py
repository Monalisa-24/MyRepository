class Robot(object):
   def __init__(self):
      self.a = 123
      self._b = 123
      self.__c = 123

obj = Robot()
print(obj.a)
print(obj._b)
print(obj._Robot__c)


class Robot(object):
   def __init__(self):
      self.__version = 22

   def getVersion(self):
      print(self.__version)

   def setVersion(self):
      self.__version = int(input("Version : "))

obj = Robot()
obj.getVersion()
obj.setVersion()
obj.getVersion()
print(obj._Robot__version)