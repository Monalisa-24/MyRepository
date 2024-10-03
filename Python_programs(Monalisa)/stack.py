# -*- coding: utf-8 -*-
"""
Created on Sat May 21 20:45:30 2022

@author: saham
"""

stack=[]
while True:
    print("\n1. push")
    print("2. pop")
    print("3. top")
    print("4. display")
    print("5. exit")
    ch=int(input("enter your choice : "))
    if(ch==1):
        stack.append(input("enter the item = "))
    if(ch==2):
        length=len(stack)
        if(length==0):
            print("stack is empty.")
        else:
            print(stack.pop(length-1),"is popped.")
    if(ch==3):
        length=len(stack)
        print("top is : ",stack[length-1])
    if(ch==4):
        length=len(stack)
        if(length==0):
            print("stack is empty.")
        else:
            print(stack,end=" ")
    if(ch==5):
        '''print("pls enter a valid choice...")
        break'''
        option=input("do you want to stop execution ?(y/n) -> ")
        if(option=='y'):
            break
        else:
            continue
    if(ch<1 or ch>5):
        print("please enter a valid choice.\n")