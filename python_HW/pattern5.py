# A
# A B
# A B C
# A B C D
# A B C D E

# n = int(input(" enter any number from 66 = "))
#
# for i in range(65, n+1):
#     for j in range(65, i + 1):
#         print(chr(j), end=" ")
#     print()

n = int(input(" enter how many rows is needed ? = "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(chr(j + 64), end=" ")
    print()
