word = input("write any word : ")
if len(word) >= 3:
    w = len(word) - 3
    s = slice(w, len(word), 1)
    n = word[s]
    if n == "ing":
        word = word + "ly"
    else:
        word = word + "ing"
    print(word)

else:
    print(word, ".....(NO CHANGE)")


