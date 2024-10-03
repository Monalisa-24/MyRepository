def avg(a, b, c):
    av = (a + b + c) / 3
    return av


x = int(input("enter the 1st number = "))
y = int(input("enter the 2nd number = "))
z = int(input("enter the 3rd number = "))

average = avg(x, y, z)
print("average = ", average)
