# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 17:26:48 2022

@author: saham
"""

'''a=int(input("Enter the first number = "))
b=int(input("Enter the second number = "))
c=int(input("Enter the third number = "))
if(a>b):
    if(a>c):
        print(a,"is greater among these 3.")
    else:
        print(c,"is greater among these 3.")
else:
    if(b>c):
        print(b,"is greater among these 3.")
    else:
        print(c,"is greater among these 3.")'''


a=int(input("Enter the first number = "))
b=int(input("Enter the second number = "))
c=int(input("Enter the third number = "))
if(a>b and a>c):
    print(a,"is greatest among 3.")
elif(b>a and b>c):
    print(b,"is greatest among 3.")
else:
    print(c,"is greatest among 3.")