# 1 2 3 4 5
# 2 3 4 5
# 3 4 5
# 4 5
# 5

n = int(input(" how many rows do you want ? = "))

for i in range(1, n + 1):
    for j in range(i, n + 1):
        print(j, end=" ")
    print()
