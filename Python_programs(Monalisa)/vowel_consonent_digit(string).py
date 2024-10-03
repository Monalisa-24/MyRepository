# -*- coding: utf-8 -*-
"""
Created on Thu May 19 22:23:27 2022

@author: saham
"""

from string import ascii_lowercase,punctuation
s="hello world 2022."
v=c=b=p=0
st=""
for i in range(len(s)):
    if s[i] in ascii_lowercase:
        st=s.upper()
print("string is : ",st)
for j in range(len(st)):
    if st[j] in 'AEIOU':
        v+=1
    elif st[j] in " ":
        b+=1
    elif st[j] in punctuation:
        p+=1
    else:
        c+=1
        

print("\n|no. of vowel = ",v)
print("|no. of consonent = ",c)
print("|no of punctuation = ",p)
print("|no. of blank = ",b)