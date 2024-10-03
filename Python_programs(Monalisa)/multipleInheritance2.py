class father():
    def __init__(self,surname):
        self.surname=surname
    def name1(self):
        print("\nfather class.")

class mother():
    def __init__(self, complextion, hairtype):
        self.complextion=complextion
        self.hairtype=hairtype
    def name2(self):
        print("\nmother class.")

class me(father,mother):
    def __init__(self,name,age,surname,complextion,hairtype):
        self.name=name
        self.age=age
        father.__init__(self,surname)
        mother.__init__(self,complextion,hairtype)
    def name3(self):
        print("\nme class.")

mycl=me("Monalisa",21,"saha","medium fair","curly")
print(mycl.name)
print(mycl.age)
print(mycl.surname)
print(mycl.complextion)
print(mycl.hairtype)
print("name : {}, age : {}, surname : {}, complextion : {}, hairtype : {}"
.format(mycl.name,mycl.age,mycl.surname,mycl.complextion,mycl.hairtype))
mycl.name1()
