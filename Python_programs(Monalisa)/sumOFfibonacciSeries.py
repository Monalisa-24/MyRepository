# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 17:23:16 2022

@author: saham
"""

n=int(input("enter a number :- "))
a=0
b=1
sum=0
print("series :- ")
for i in range(1,n+1):
    print(a)
    sum=sum+a
    fibo=a+b
    a=b
    b=fibo
print("sum of the series = ", sum)