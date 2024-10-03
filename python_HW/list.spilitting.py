mylist = []
positive = []
negative = []

n = int(input("enter the number into the list = "))
for i in range(0, n):
    number = int(input("enter the number  %d elements :" % i))
    mylist.append(number)

print("The list is = ", mylist)

for j in range(n):
    if mylist[j] >= 0:
        positive.append(mylist[j])
    else:
        negative.append(mylist[j])
print("the positive list is = ", positive)
print("the negative list is = ", negative)
