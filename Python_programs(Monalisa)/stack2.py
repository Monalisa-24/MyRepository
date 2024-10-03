# -*- coding: utf-8 -*-
"""
Created on Sun May 22 00:23:33 2022

@author: saham
"""

stack=[]


def push():
    stack.append(int(input("enter the item = ")))
def pop():
    length=len(stack)
    if(length==0):
        print("stack is empty.")
    else:
        print(stack.pop(length-1),"is popped.")
    
while True:
    print("\n1.push  2.pop   3.diplay   4.exit/n")
    ch=int(input("enter your choice : "))
    
    if(ch==1):
        push()
    if(ch==2):
        pop()
    if(ch==3):
        length=len(stack)
        if(length==0):
            print("stack is empty.")
        else:
            print(stack,end=" ")
    if(ch==4):
        option=input("do you want to stop execution ?(y/n) -> ")
        if(option=='y'):
            break
        else:
            continue
    if(ch<1 or ch>4):
        print("please enter a valid choice.\n")
        