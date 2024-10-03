# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 15:49:45 2022

@author: saham
"""

#doing explicit type-casting
'''numb=int(input("Enter a number :- "))
temp=numb
numb_s=str(numb)
length=len(numb_s)
sum=0
while(numb!=0):
    rem=numb%10
    sum=sum+(rem**length)
    numb//=10
if(sum==temp):
    print(temp,"Armstrong number.")
else:
    print(temp,"not armstrong number.")
'''
#......................................#
numb=int(input("Enter a number :- "))
temp=numb
temp2=temp
sum=0
c=0
while(temp!=0):
    c+=1
    temp//=10
print("number of digit = ",c)
while(numb!=0):
    rem=numb%10
    sum=sum+(rem**c)
    numb//=10
if(sum==temp2):
    print(temp2,"Armstrong number.")
else:
    print(temp2,"not armstrong number.")
    
    