#       1
#     2 1
#   3 2 1
# 4 3 2 1

n = int(input(" how many rows do you want ? = "))

for i in range(n):
    for j in range(n - i - 1):
        print(" ", end=" ")
    for k in range(i, -1, -1):
        print(k + 1, end=" ")
    print()
