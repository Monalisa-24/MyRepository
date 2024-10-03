n = int(input("enter the term :- "))
sum = 0
a = 1
c = 1
while c <= n:
    sum = sum + a
    a = (a * 10) + 1
    c = c + 1

print("the sum of the series = ", sum)
