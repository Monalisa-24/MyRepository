# -*- coding: utf-8 -*-
"""
Created on Tue May 31 23:02:48 2022

@author: saham
"""

class student:
    def __init__(self,name,grade,age) :
        self.name=name
        self.grade=grade
        self.age=age
    def display(self):
        print("name of the student",self.name)
        print("grade of the student",self.grade)
        print("age of the student",self.age)
rahul=student("Rahul","A","12")
sanu=student("sanu","A","12")
dev=student("dev","A","12")
rahul.display()
sanu.display()
dev.display()