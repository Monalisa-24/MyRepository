# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 21:58:08 2022

@author: saham
"""

s=str(input("type a string :- "))
s=s.split()
print("now the words are = ", s)
for word in s:
    if(len(word)%2==0):
        print("even length words are :- \n",word)
    else:
        print("odd length words are :- \n",word)
        

