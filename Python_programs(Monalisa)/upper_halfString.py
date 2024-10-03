# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 22:21:25 2022

@author: saham
"""

s=str(input("type a word :- "))
length=len(s)
print("length is:- ",length)
half=length//2
print(half)
HU=' '
for i in range(0,length):
    if i >= half:
        HU+=s[i]
    else:
        HU+=s[i].upper()
print("afetr operation :- ",HU)