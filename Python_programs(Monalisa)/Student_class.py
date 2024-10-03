class student:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
    def display(self):
        print("name  : ",self.name)
        print("age   : ",self.age)
        print("grade : ",self.grade)

print("\nfor 1st student : ")
s1=student("Aritra",20,"A")
s1.display()
print("\nfor 2nd student : ")
s2=student("Arvind", 20, "B")
s2.display()
print("\nfor 3rd student : ")
s3=student("Arnab", 20, "C")
s3.display()
print("\nfor 4th student : ")
s4=student("Akash", 20, "D")
s4.display()
print("\nfor 5th student : ")
s5=student("Ahir", 20, "E")
s5.display()

