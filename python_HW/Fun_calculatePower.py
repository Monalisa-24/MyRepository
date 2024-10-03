# def findPower(a, b):
#     c = 1
#     while b != 0:
#         c = c * a
#         b -= 1
#     return c
#
#
# x = int(input("Enter the base -> "))
# y = int(input("Enter the exponent -> "))
#
# result = findPower(x, y)
# print("The result is =", result)


def power(x, y):
    z = 1
    i = 1
    if (y == 0):
        z = 1
    else:
        while (i <= y):
            z = z * x
            i += 1
        return z


m = int(input("enter the base = "))
n = int(input("enter the exponent = "))
power1 = power(m, n)
print(m, " to the power of", n, "is", power1)
