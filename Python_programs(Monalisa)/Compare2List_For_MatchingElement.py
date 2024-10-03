# -*- coding: utf-8 -*-
"""
Created on Mon May  9 08:55:53 2022

@author: saham
"""
#compare 2 lists and find out the common element.

n1=int(input("enter the range of the List_c1 :- "))
List_c1=[]
for i in range(n1):
    item1=str(input("enter the items for List_c1 = "))
    List_c1.append(item1)
print(List_c1)


n2=int(input("enter the range of the List_c2 :- "))
List_c2=[]
for i in range(n2):
    item2=str(input("enter the items for List_c2 = "))
    List_c2.append(item2)
print(List_c2)


flag=False
common_list=[]
for i in range(len(List_c1)):
    for j in range(len(List_c2)):
        if(List_c1[i]==List_c2[j]):
            flag=True
            common_list.append(List_c1[j])
            
'''if(len(List_c1)>len(List_c2) or len(List_c1)<len(List_c2)):
   print("length doesn't match.")'''
if(flag==True):
    print("common elements found :-), and the element is = ", common_list)
else:
    print("common elements not found :-(")