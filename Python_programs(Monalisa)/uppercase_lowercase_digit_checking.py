# -*- coding: utf-8 -*-
"""
Created on Thu May 19 23:08:28 2022

@author: saham
"""

from string import ascii_uppercase,ascii_lowercase,digits

s="HellO WorLd 2022"

u=l=d=b=0
for i in range(len(s)):
    if s[i] in ascii_uppercase:
        u+=1
    elif s[i] in ascii_lowercase:
        l+=1
    elif s[i] in digits:
        d+=1
    else:
        b+=1
        
        
print("uppercase = ",u)
print("lowercase = ",l)
print("digit = ",d)
print("space = ",b)
        