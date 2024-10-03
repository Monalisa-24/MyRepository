import string

f = open("demofile3.txt", "r")
a = f.read()
print(a)
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
f.close()
