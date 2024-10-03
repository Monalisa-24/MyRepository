# -*- coding: utf-8 -*-
'''check if a string has atleast one letter and one digit
  .......................................................'''

def StringChecjking(s):

    flag_l=False
    flag_d=False

    for i in s:
        if i.isalpha():
            flag_l=True
        if i.isdigit():
            flag_d=True
    return flag_l and flag_d


s=str(input("type a string:- "))
print(StringChecjking(s))