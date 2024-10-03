# *
#   ***
#  *****
# *******

n = int(input("enter the number to n = "))

# for i in range(1, n + 1):
#     for j in range(1, (n + 1) - i):
#         print(" ", end="")
#     for k in range(1, (2*i-1)+1):
#         print("*", end="")
#     print("\n")

for i in range(1, n + 1):
    for j in range(1, n - i + 1):
        print(end="  ")
    for k in range(1, i + 1):
        print("*", end=" ")
    for m in range(2, i + 1):
        print("*", end=" ")
    print()

# for i in range(1, n + 1):
#     for j in range(1, n - i + 1):
#         print(end="  ")
#     for k in range(1, 2 * i):
#         print("*", end=" ")
#     print()
