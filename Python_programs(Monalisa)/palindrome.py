# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 17:08:40 2022

@author: saham
"""

numb=int(input("enter a number :- "))
temp=numb
rev=0
while(numb!=0):
    rem=numb%10
    rev=(rev*10)+rem
    numb//=10
print(rev)
if(rev==temp):
  print(temp,"is a palindrome number.")
else:
    print(temp,"is not a palindrome number.")