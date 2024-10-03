# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 20:11:22 2022

@author: saham
"""

def gcd(x,y,z):
    if y>x:
        return gcd(y,x,z)
    elif(x%y==0):
        return y
    else:
        return gcd(z,gcd(y,x%y,z),x)
    
a=float(input("enter the first number :- "))
b=float(input("enter the second number :- "))
c=float(input("enter the third number :- "))
print(gcd(a,b,c))
#print("\nthe gcd of these numbers = ",g)