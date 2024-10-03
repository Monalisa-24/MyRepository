# def remove(word):
#     return word.replace(" ", "")
#
#
# word1 = 'Monalisa   Saha'
# print(remove(word1))


# a=input("Enter any string")
# a=a.split()
# s=""
# for i in range (len(a)):
#     s=s+a[i]+" "
# print(s)

a = input("Enter any string : ")
words = a.split()
s = " ". join(words)
print(s)