# def count(string1):
#     vowels = consonants = digits = whitespaces = punctuation = 0
#     for i in range(0, len(string1)):
#         ch = string1[i]
#         if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
#             ch = ch.lower()
#             if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
#                 vowels += 1
#             else:
#                 consonants += 1
#         elif '0' <= ch <= '9':
#             digits += 1
#         elif ch == " ":
#             whitespaces += 1
#         else:
#             punctuation += 1
#     print("Vowels = ", vowels)
#     print("Consonants = ", consonants)
#     print("Digits = ", digits)
#     print("WhiteSpaces = ", whitespaces)
#     print("Punctuation = ", punctuation)
#
#
# string2 = "! MOnalisA Saha/2001 ?"
# count(string2)


import string

a = input("Enter any string = ")
vowels = 0
consonant = 0
digit = 0
punctuations = 0
space = 0
for i in range(len(a)):
    if a[i] in "AEIOUaeiou":
        vowels = vowels + 1
    elif a[i] >= 'A' or 'a' <= a[i] <= 'Z' or a[i] >= 'z':
        consonant = consonant + 1
    elif '0' <= a[i] <= '9':
        digit = digit + 1
    elif a[i] in string.punctuation:
        punctuations = punctuations + 1
    else:
        space = space + 1
print(vowels)
print(consonant)
print(digit)
print(punctuations)
print(space)
