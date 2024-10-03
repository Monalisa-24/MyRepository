# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 17:21:48 2022

@author: saham
"""

n=int(input("enter a number :- "))
product=1
while(n!=0):
    rem=n%10
    product=product*rem
    n//=10
print("Product of digit is =",product)