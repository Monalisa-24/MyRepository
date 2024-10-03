n = int(input("enter the value of n = "))
a = 0
b = 1
c = 1
f = 0

print("The Fibonacci Series = ")
while c <= n:
    print(a)
    f = a + b
    a = b
    b = f
    c = c + 1
