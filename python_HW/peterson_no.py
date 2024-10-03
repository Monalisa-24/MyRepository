import math

n = int(input("enter any number = "))
r = 0
s = 0
fact = 0
temp = n

while n > 0:
    r = n % 10
    fact = math.factorial(r)
    s = s + fact
    n = n // 10

if s == temp:
    print("the number is a peterson number.")
else:
    print("the number isn't a peterson number.")
