# -*- coding: utf-8 -*-
"""
Created on Fri May 20 23:39:23 2022

@author: saham
"""

s="There are some fruits in this busket"
w=s.split()
print(w)
w.sort(key=len,reverse=True)
newString=" ".join(w)
        
print("after sorting : ",newString)
nw=newString.split()
for i in range(len(nw)):
    print(nw[i],"-",len(nw[i]))
        
        
    
        
        