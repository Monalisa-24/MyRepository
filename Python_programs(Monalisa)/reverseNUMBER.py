# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 17:14:59 2022

@author: saham
"""

numb=int(input("enter a number :- "))
temp=numb
sum=0
rev=0
while(numb>0):
    rem=numb%10
    rev=(rev*10)+rem
    numb//=10
print("reverse of ",temp," is = ",rev)