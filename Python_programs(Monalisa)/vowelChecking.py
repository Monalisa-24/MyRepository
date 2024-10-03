# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 17:37:47 2022

@author: saham
"""

alphabet=str(input("enter a alphabet :- "))
a=alphabet.upper()
print(a)
if(a=='A' or a=='E' or a=='I' or a=='O' or a=='U'):
    print(a,"is a vowel.")
else:
    print(a,"is not a vowel.")