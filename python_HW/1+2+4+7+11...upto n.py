n = int(input("enter the number of terms = "))
i = 1
s = 0
c = 1
d = 1

while c <= n:
    s = s + i
    i = i + d
    d = d + 1
    c = c + 1

print("the sum of the series = ", s)
