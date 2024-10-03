n = int(input("enter any number = "))
d = 0
r = 0
print("\nthe odd digits in this entered number = ")

while n > 0:
    d = n % 10
    n = n // 10
    r = d % 2
    if r != 0:
        print("\n", d)

