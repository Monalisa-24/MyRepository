# max between 5 inputted numbers

a = int(input("enter the 1st number : "))
b = int(input("enter the 2nd number : "))
c = int(input("enter the 3rd number : "))
d = int(input("enter the 4th number : "))
e = int(input("enter the 5th number : "))

mxm = a

if mxm < b:
    mxm = b
if mxm < c:
    mxm = c
if mxm < d:
    mxm = d
if mxm < e:
    mxm = e
print(" max = ", mxm)