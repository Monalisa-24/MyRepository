# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 23:45:02 2022

@author: saham
"""

'''s=str(input("type a word :- "))
length=len(s)
string=' '
for i in range(0,length):
    if(i>0 and i<length-1):
        string+=s[i]
    else:
        string+=s[i].capitalize()
print("after operation :- ",string)'''



s=str(input("type a word :- "))
s=s.title()
print(s)
s=s.split()
print(s)
string=' '
for word in s:
    #string=word[:-1]
    #print(string)
    string+=word[:-1]+word[-1].capitalize()+" "
print(string)
        
