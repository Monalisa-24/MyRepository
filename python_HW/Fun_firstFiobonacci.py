def fibonacci(n):
    a = 0
    b = 1
    for i in range(0, n, 1):
        print(a, end=' ')
        c = a + b
        a = b
        b = c


m = int(input(" Enter the number of term to display :- "))
if m <= 0:
    print("Error...!\nProgram is ended.")
else:
    print("The fibonacci series :- ")
    fibonacci(m)

