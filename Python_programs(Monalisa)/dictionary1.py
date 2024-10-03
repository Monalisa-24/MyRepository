# -*- coding: utf-8 -*-
"""
Created on Sat May 21 21:46:11 2022

@author: saham
"""

dictionary={'Ram':10,'Shyam':20,'Yadu':30}
print(dictionary)
k=input("enter the key to know if it is present or not ! -> \n")
key=k.title()
present=key in dictionary
print(present)
print("Values are = ",dictionary.values())
print("sum of the values = ",sum(dictionary.values()))