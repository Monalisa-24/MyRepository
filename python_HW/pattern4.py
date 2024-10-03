# 1
# 1 0
# 1 0 1
# 1 0 1 0
# 1 0 1 0 1

n = int(input(" how many rows do you want ? = "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j % 2, end="")
    print()
