# -*- coding: utf-8 -*-
"""
Created on Tue May 31 21:15:07 2022

@author: saham
"""

from string import ascii_uppercase,ascii_lowercase,digits
p=input("create your password : ")
l=len(p)
u=lo=d=w=0
if(l<6):
    print("Password is too short !\nThis should be between 6 to 12.")
elif(l>=6 and l<=12):
    for i in p:
        if(i in ascii_uppercase):
            u+=1
        if(i in ascii_lowercase):
            lo+=1
        if(i in digits):
            d+=1
        if(i=='@' or i=='#' or i=='$'):
            w+=1
    print(u,lo,d,w)    
    if(lo>0 and u>0 and d>0 and w>0):
        print("Valid Password.. :-)")
    else:
        print("Invalid password.. :-(")
else:
    print("Password is too long !\nThis should be between 6 to 12.")

