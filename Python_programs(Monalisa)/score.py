# -*- coding: utf-8 -*-
"""
Created on Sat May 21 22:47:44 2022

@author: saham
"""
print("\n***enter the score between 0.0 and 1.0***")
while True:
    score=float(input("enter the score :- "))
    if(score>=0.0 and score<0.6):
        print("F")
        break
    if(score>=0.6 and score<=0.7):
        print("D")
        break
    if(score>=0.7 and score<=0.8):
        print("C")
        break
    if(score>=0.8 and score<=0.9):
        print("B")
        break
    if(score>=0.9 and score<=1.0):
        print("A")
        break
    if(score>=1.0 or score<=0.0):
        print("Error !!!  try again...")
        continue