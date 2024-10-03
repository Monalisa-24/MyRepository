# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 20:15:07 2022

@author: saham
"""

txt=str(input("enter a word :- "))
txt1=" "
n=int(input("enter the position you want the letter to  be cut :- "))
for i in range(0,len(txt)):
    if(i!=n):
        txt1=txt1+txt[i]
print("now the word is :- ",txt1)