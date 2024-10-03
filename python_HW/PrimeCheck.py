n = int(input("Enter a positive number except 1 : "))
i = 2
flag = 0

while i <= n/2:
    if n % i == 0:
        flag = 1
        break
    i += 1

if flag == 0:
    print("the number is a prime number")
else:
    print("the number isn't a prime number")
