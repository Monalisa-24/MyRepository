#  * * * * *
#  *       *
#  *       *
#  *       *
#  * * * * *

# n = int(input("enter the range for row & column = "))
#
# for i in range(n):
#     for j in range(n):
#         if i == 0 or i == n - 1 or j == 0 or j == n - 1:
#             print("*", end=' ')
#         else:
#             print(" ", end=' ')
#     print()

a = int(input("enter the range for row & column = "))

for i in range(1, a + 1):
    for j in range(1, a + 1):
        if i == 1 or i == a or j == 1 or j == a:
            print("*", end=' ')
        else:
            print(end='  ')
    print()
