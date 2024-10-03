# -*- coding: utf-8 -*-
"""
Created on Thu May 19 23:56:45 2022

@author: saham
"""

s=input("take string as input : ")
st=s.upper()
w=st[::-1]
if(st==w):
    print("yes, |",s,"| is palindrome.")
else:
    print("no, |",s,"| is not palindrome.")
    
    
