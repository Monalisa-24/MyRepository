def rePower(a, b):
    if a == 0:
        return a
    elif b == 0:
        return 1
    elif b == 1:
        return a
    else:
        return a * rePower(a, b - 1)


x = int(input("Enter the base -> "))
y = int(input("Enter the exponent -> "))
result = rePower(x, y)
print("The result is =", result)
