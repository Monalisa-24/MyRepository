# def longestWord(list1):
#     max_len = -1
#     result = 0
#     for i in list1:
#         if len(i) > max_len:
#             max_len = len(i)
#             result = i
#     print("longest string is = ", result)
#     print("and the length is = ", len(result))
#
#
# list2 = ['Kolkata', 'Delhi', 'Mumbai', 'Goa', 'darjeeling']
# longestWord(list2)

sentence = input("enter a sentence : ")
words = sentence.split()
print(words)
longest = max(words, key=len)
print("longest word is : ", longest)
print("and the length is: ", len(longest))
