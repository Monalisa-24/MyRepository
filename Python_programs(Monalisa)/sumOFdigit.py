# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 17:19:40 2022

@author: saham
"""

n=int(input("enter a number :- "))
sum=0
while(n!=0):
    rem=n%10
    sum=sum+rem
    n//=10
print("Sum of digit is =",sum)