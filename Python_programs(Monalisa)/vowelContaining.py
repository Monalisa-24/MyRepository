# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 20:38:10 2022

@author: saham
"""

def vowelContaining(string):
    string=string.lower()
    print(string)
    vowel=set('aeiou')
    print("length of vowel =",len(vowel))
    s=set({})
    for i in string:
        if i in vowel:
            s.add(i)
    print("updated s = ",s)
            
    print("length of s =",len(s))
    if len(s)==len(vowel):
        print("accepted.")
    else:
        print("not accepted.")
            
string=str(input("type a string :- "))
vowelContaining(string)