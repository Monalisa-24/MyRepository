# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 16:36:01 2022

@author: saham
"""

numb=int(input("enter a number :- "))
temp=numb
sum=0
#f=1
while(numb>0):
    rem=numb%10
    f=1
    for i in range(1,rem+1):
        f=f*i
    sum=sum+f
    numb//=10
if(sum==temp):
    print(temp,"krishnamurty number.")
else:
    print(temp,"not krishnamurty number.")