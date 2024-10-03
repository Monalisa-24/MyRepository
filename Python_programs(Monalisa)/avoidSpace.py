# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 19:58:14 2022

@author: saham
"""

txt=str(input("enter a string:- \n"))
length=len(txt)
print(length)
count=0
for i in range(0,length):
    if(txt[i]==" "):
        count+=0
    else:
        count+=1
print("now after operation :- \n",count)
