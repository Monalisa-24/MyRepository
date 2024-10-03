# 1 2 3 4
#   1 2 3
#     1 2
#       1

n = int(input(" how many rows do you want ? = "))

for i in range(n, 0, -1):
    for j in range(1, (n + 1) - i):
        print(" ", end=" ")
    for k in range(1, i + 1):
        print(k, end=" ")
    print()
