# -*- coding: utf-8 -*-
"""
Created on Tue May 31 19:48:22 2022

@author: saham
"""
class Password:
    check=" Check Password Validity...\n----------------------------"
    @classmethod
    def password(cls,p):
        from string import ascii_uppercase,ascii_lowercase,digits
        #print(cls.check)
        length=len(p)
        u=l=d=w=0
        if(length>=6 and length<=12):
            for i in p:
                if(i in ascii_uppercase):
                    u+=1
                if(i in ascii_lowercase):
                    l+=1
                if(i in digits):
                    d+=1
                if(i=='@' or i=='#' or i=='$'):
                    w+=1
            if(l>0 and u>0 and d>0 and w>0):
                print("Valid Password.. :-)🤩")
            else:
                print("Invalid password.. :-(😢")
        elif(length<6):
            print("Password is too short !\nThis should be between 6 to 12.🙁")
        else:
            print("Password is too long !\nThis should be between 6 to 12.🥱")
        
    
    
pw=Password()
print(pw.check)
pswrd=input("create your password🙂 : ")
Password.password(pswrd)
                
            