from abc import ABC, abstractmethod

class Student(ABC):
	Name=None
	Contact=None
	City=None
	@abstractmethod
	def getdata():
		pass
	@abstractmethod
	def display():
		pass
class BCA(Student):
	Sub_Combination=None
	Sub_Spelialization=None
class BBA(Student):
	Sub_Combination=None
	Sub_Spelialization=None

a=BCA()
a.getdata()
a.display()

b=BBA()
b.getdata()
b.display()