sentence = input(" write a sentence : ")
w = sentence.split(" ")
print(w)
new_word = [i[:: -1] for i in w]
print(new_word)
new_sentence = " ".join(new_word)
print(new_sentence)


# for i in range(len(w)):
#     s = w[i]
#
#     w[i] = s[:: - 1]
# new_sentence = " ".join(w)
# print(new_sentence, end=" ")

