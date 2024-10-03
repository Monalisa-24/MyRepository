# -*- coding: utf-8 -*-
"""
Created on Thu May 19 23:16:01 2022

@author: saham
"""

l=[]
p_sum=0
n_sum=0
t_sum=0
print("\nenter 5 numbers below\n")
for i in range(0,5):
    n=int(input("take input : "))
    if(n>0):
        p_sum+=n
    else:
        n_sum+=n
    t_sum+=n
    l.append(n)
print("numbers are :", l)

avg=(t_sum/len(l))
print("sum of positive number = ",p_sum)
print("sum of negative number = ",n_sum)
print("sum of total number = ",t_sum)

print("average of total number = ",avg)
print("greater than average : ")
for i in range(len(l)):
    if(l[i]>avg):
        print(l[i],end=" ")






        