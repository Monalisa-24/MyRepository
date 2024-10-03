# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 17:49:52 2022

@author: saham
"""

n=int(input("enter a number :- "))
temp=n
even,odd,c=0,0,0
while temp!=0:
    c+=1
    temp//=10
print("number of digit =",c)
while n!=0 :
    rem=n%10
    if(rem%2==0):
        even+=1
    else:
        odd+=1
    n//=10
print("The number of even number is = ",even)
print("The number of odd number is = ",odd)