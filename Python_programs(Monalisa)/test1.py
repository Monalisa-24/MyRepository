# -*- coding: utf-8 -*-
"""
Created on Thu May 19 22:46:52 2022

@author: saham
"""

from string import ascii_lowercase
s=" hll wrld"
for i in range(len(s)):
    if s[i] in ascii_lowercase:
        st=s.upper()
        print(st)