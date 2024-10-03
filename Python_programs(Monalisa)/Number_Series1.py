# -*- coding: utf-8 -*-
"""
Created on Sat May 21 22:45:41 2022

@author: saham
"""

n=int(input("enter number of term"))
s=0
for i in range(1,n+1):
    s+=(1/i)
print(s)