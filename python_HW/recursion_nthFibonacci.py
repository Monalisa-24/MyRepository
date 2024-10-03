# def reFibonacci(n):
#
#     if (n == 0) or (n == 1):
#         return n
#     else:
#         return reFibonacci(n - 1) + reFibonacci(n - 2)
#
#
# m = int(input("Enter the number of term to display :- "))
# if m <= 0:
#     print("Error...!\nProgram is ended.")
# else:
#     print("The fibonacci series :- ")
#     for i in range(0, m, 1):
#         print(reFibonacci(i))

# def reFibonacci(n):
#     if n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return reFibonacci(n - 1) + reFibonacci(n - 2)
#
#
# m = int(input("Enter the number of term to display :- "))
# print(m, "th fibonacci term:", reFibonacci(m))
# print("The fibonacci series :- ")
# for i in range(1, m + 1, 1):
#     print(reFibonacci(i), end=' ')

def reFibonacci(n):
    if n <= 2:
        return n - 1
    else:
        return reFibonacci(n - 1) + reFibonacci(n - 2)


m = int(input("Enter the number of term to display :- "))
if m <= 0:
    print("Error...!\nProgram is ended.")
else:
    print("The fibonacci series :- ")
    for i in range(1, m + 1, 1):
        print(reFibonacci(i))
