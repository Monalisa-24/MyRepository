def d2b(n):
    if n > 0:
        r = n % 2
        d2b(n // 2)
        print(r, end='')


m = int(input("enter a decimal number : "))
print("The converted binary : ", end='')
d2b(m)
