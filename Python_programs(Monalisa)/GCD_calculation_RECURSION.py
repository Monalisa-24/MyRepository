# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 19:58:42 2022

@author: saham
"""

def gcd(x,y):
    if(y>x):
        return gcd(y,x)
    elif(x%y==0):
        return y
    else:
        return gcd(y,x%y)
    
a=float(input("enter the first number :- "))
b=float(input("enter the second number :- "))
g=gcd(a,b)
print("\nthe gcd of these numbers = ",g)