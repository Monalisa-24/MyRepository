# max between 3 inputted numbers

x = int(input("enter the 1st number : "))
y = int(input("enter the 2nd number : "))
z = int(input("enter the 3rd number : "))

# if (x >= y) and (x >= z):
#     print(" 1st num is max : ", x)
# elif (y >= z) and (y >= x):
#     print(" 2nd num is max : ", y)
# else:
#     print("3rd num  is max : ", z)

mxm = x

if mxm < y:
    mxm = y
if mxm < z:
    mxm = z
print(" max = ", mxm)


