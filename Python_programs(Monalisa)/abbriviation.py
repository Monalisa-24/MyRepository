# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 20:35:34 2022

@author: saham
"""

name=str(input("Enter your name :- \n"))
print(name)
n=len(name)
print(n)
fn=name[:1]
print(fn)
for i in range(1,n+1):
    if(name[i]==" "):
        break
ln=name[(i+1):]
print(ln)
print("abbriviation of your name =",fn+"."+ln)
