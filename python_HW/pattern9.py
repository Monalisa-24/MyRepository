# 4321
#  432
#   43
#    4

n = int(input(" how many rows do you want ? = "))

for i in range(n):
    for j in range(i):
        print(" ", end=" ")
    for k in range(n - i):
        print(n - k, end=" ")
    print()
