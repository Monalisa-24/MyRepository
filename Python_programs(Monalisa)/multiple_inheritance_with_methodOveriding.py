class father:
    def __init__(self,surname):
        self.surname=surname
    def display(self):
        print("surname : ",self.surname)
class mother:
    def __init__(self,hairtype):
        self.hairtype=hairtype
    def display(self):
        print("hairtype : ",self.hairtype)
class me(mother,father):
    def __init__(self,name,surname,hairtype):
        self.name=name
        father.__init__(self,surname)
        mother.__init__(self,hairtype)
    

myobj=me("Monalisa","Saha","Wavey")
print("name : {}, surname : {}, hairtype : {}".format(myobj.name,myobj.surname,myobj.hairtype))
myobj.display()
