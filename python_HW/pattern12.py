# 1 2 3 4 3 2 1
#   1 2 3 2 1
#     1 2 1
#       1
#     ......

n = int(input(" Enter the number of rows..."))

for i in range(n, 0, -1):
    for j in range(1, (n + 1) - i):
        print(" ", end=" ")
    for j in range(1, i + 1):
        print(j, end=" ")
    for j in range(i - 1, 0, -1):
        print(j, end=' ')
    print()

