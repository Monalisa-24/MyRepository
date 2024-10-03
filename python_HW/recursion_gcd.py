def findGcd(a, b):
    # while a != b:
    if b == 0:
        return a
    else:
        return findGcd(b, a % b)


n1 = int(input("enter an integer number = "))
n2 = int(input("enter an integer number = "))
GCD = findGcd(n1, n2)
print("GCD = ", GCD)
