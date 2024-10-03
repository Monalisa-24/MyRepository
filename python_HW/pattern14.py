#       4
#     4 3 4
#   4 3 2 3 4
# 4 3 2 1 2 3 4
#   4 3 2 3 4
#     4 3 4
#       4

n = int(input(" how many rows do you want ? = "))

for i in range(n, 0, -1):
    for j in range(1, i):
        print(" ", end=' ')
    for j in range(n, i - 1, -1):
        print(j, end=' ')
    for j in range(i + 1, n + 1):
        print(j, end=' ')
    print()

for i in range(n, 1, -1):
    for j in range((n + 1) - i):
        print(" ", end=' ')
    for j in range(n, n - i + 1, -1):
        print(j , end=' ')
    for j in range(n - i + 3, n + 1):
        print(j, end=' ')
    print()
