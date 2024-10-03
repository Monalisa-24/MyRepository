# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 20:45:02 2022

@author: saham
"""
def POD(n):
    product=1
    while(n!=0):
        rem=n%10
        product=product*rem
        n//=10
    print("Product of digit is =",product)

def SOD(n):
    sum=0
    while(n!=0):
        rem=n%10
        sum=sum+rem
        n//=10
    print("Sum of digit is =",sum)
    
def armstrong(n):
    temp=n
    temp2=temp
    sum=0
    c=0
    while(temp!=0):
        c+=1
        temp//=10
    print("number of digit = ",c)
    while(n!=0):
        rem=n%10
        sum=sum+(rem**c)
        n//=10
    if(sum==temp2):
        print(temp2,"Armstrong number.")
    else:
        print(temp2,"not armstrong number.")
        
def peterson(n):
    temp=n
    sum=0
    #f=1
    while(n>0):
        rem=n%10
        f=1
        for i in range(1,rem+1):
            f=f*i
        sum=sum+f
        n//=10
    if(sum==temp):
        print(temp,"Peterson number.")
    else:
        print(temp,"not Peterson number.")

def palindrome(n):
    temp=n
    rev=0
    while(n!=0):
        rem=n%10
        rev=(rev*10)+rem
        n//=10
    print(rev)
    if(rev==temp):
      print(temp,"is a palindrome number.")
    else:
        print(temp,"is not a palindrome number.")
        
def EvenOddCount(n):
    temp=n
    even,odd,c=0,0,0
    while temp!=0:
        c+=1
        temp//=10
    print("number of digit =",c)
    while n!=0 :
        rem=n%10
        if(rem%2==0):
            even+=1
        else:
            odd+=1
        n//=10
    print("The number of even number is = ",even)
    print("The number of odd number is = ",odd)
    
def Reverse_number(n):
    temp=n
    rev=0
    while(n>0):
        rem=n%10
        rev=(rev*10)+rem
        n//=10
    print("reverse of ",temp," is = ",rev)
    
    
#def check():
number=int(input("enter a number :- \n"))
while True:
    print("\n\n-:.........YOUR OPTIONS.........:-\n")
    print("1.PRODUCT of DIGIT\n2.SUM of DIGIT\n3.CHECK ARMSTRONG\n4.CHECK PETERSON\n5.CHECK PALINDROME\n6.EvenOddCount\n7.REVERSE THE NUMBER\n")
    opt=int(input("\nSelect your options :- \n"))
    
    if(opt==1):
        POD(number)
    if(opt==2):
        SOD(number)
    if(opt==3):
        armstrong(number)
    if(opt==4):
        peterson(number)
    if(opt==5):
        palindrome(number)
    if(opt==6):
        EvenOddCount(number)
    if(opt==7):
        Reverse_number(number)
    if(opt!=1 and opt!=2 and opt!=3 and opt!=4 and opt!=5 and opt!=6 and opt!=7):
        print("\nenter a valid option !!!\n")
        break
#check()
    







