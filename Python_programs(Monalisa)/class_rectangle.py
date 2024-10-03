# -*- coding: utf-8 -*-
"""
Created on Tue May 31 22:53:35 2022

@author: saham
"""
class Rectangle:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def Area(self):
        self.area= self.a*self.b
        
    def __gt__(self,other):
        return self.area>other.area
            
           
obj1=Rectangle(30,20)
obj1.Area()
obj=Rectangle(30,30)
obj.Area()
if(obj1 > obj):
    print("First one is greater.")
else:
    print("Second one is greater.") 
    
    
    
    
    
    
    
