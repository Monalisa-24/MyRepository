n = int(input("enter any number = "))
r = 0
s = 0
temp = n

while n > 0:
    r = n % 10
    n = n // 10
    s = pow(r, 3) + s

if temp == s:
    print("the number is an armstrong number.")
else:
    print("the number isn't an armstrong number.")
