# 1
# 2 1
# 3 2 1
# 4 3 2 1

n = int(input(" how many rows do you want ? = "))

for i in range(1, n + 1):
    for j in range(i - 1, -1, -1):
        print(j + 1, end=" ")
    print()
