class grandpa:
    def __init__(self,surname):
        self.surname=surname
    def name1(self):
        print("grandpa class.")

class father(grandpa):
    def __init__(self,haircolor,surname):
        super().__init__(surname)
        self.haircolor=haircolor
    def name2(self):
        print("father class.")

class me(father):
    def __init__(self,haircolor,surname,face_shape):
        super().__init__(haircolor,surname)
        self.face_shape=face_shape
    def name3(self):
        print("me class.")
    

i=me("black","saha","round")
print(i.haircolor)
print(i.surname)
print(i.face_shape)
i.name1()
print("haircolor : {}, surname : {}, face_shape : {}".format(i.haircolor, i.surname, i.face_shape))