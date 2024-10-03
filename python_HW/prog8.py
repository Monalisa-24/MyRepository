# n = int(input(" enter a number : "))
# f = 1
#
# while n > 1:
#     f = f * n
#     n -= 1
# print(" factorial = ", f)
# .........................................................................................

n = int(input(" enter a number : "))
f = 1
i = 1

while i <= n:
    f = f * i
    i += 1
print(" factorial = ", f)
