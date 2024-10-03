n = int(input("enter the term = "))
a = 1
sum = 0
c = 1


while c <= n:
    sum = sum + a ** c
    a = a + 2
    c += 1
print("sum = ",sum)