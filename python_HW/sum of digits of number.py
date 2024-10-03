n = int(input("Enter any number :  "))
d = 0
s = 0
while n > 0:
    d = n % 10
    s = s + d
    n = n//10
print("the sum of digits of these numbers : ", s)



