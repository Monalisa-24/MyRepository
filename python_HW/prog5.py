# max between 5 inputted numbers

a = int(input("enter the 1st number : "))
b = int(input("enter the 2nd number : "))
c = int(input("enter the 3rd number : "))
d = int(input("enter the 4th number : "))
e = int(input("enter the 5th number : "))

if (a > b) and (a > c) and (a > d) and (a > e):
    print(" 1st num is max : ", a)
elif (b > c) and (b > d) and (b > e):
    print(" 2nd num is max : ", b)
elif (c > d) and (c > e):
    print(" 3rd num is max : ", c)
elif d > e:
    print(" 4th num is max : ", d)
else:
    print(" 5th num  is max : ", e)
