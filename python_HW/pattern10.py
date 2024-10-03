#    4
#   43
#  432
# 4321

# n = int(input(" how many rows do you want ? = "))
#
# for i in range(n):
#     for j in range(n - i -1):
#         print(" ", end=" ")
#     for k in range(i + 1):
#         print(n - k, end=" ")
#     print()


n = int(input(" how many rows do you want ? = "))

for i in range(1, n + 1):
    for j in range(1, n - i + 1):
        print(" ", end=" ")
    for k in range(n, n - i, - 1):
        print(k, end=" ")
    print()
