def binarySearch(the_list, x):
    low = 0
    high = len(the_list) - 1
    while low <= high:
        mid = (high + low) // 2
        if the_list[mid] == x:
            return mid
        elif the_list[mid] > x:
            return mid - 1
        else:
            return mid + 1
    return -1


my_list = []
n = int(input("enter the number of elements of the list : "))
for i in range(0, n):
    number = int(input("enter the number  %d elements :" % i))
    my_list.append(number)
print(my_list)
num = int(input("Enter the number for searching : "))
r = binarySearch(my_list, num)

if r == -1:
    print("%d isn't present at index....." % num)
else:
    print("%d is present at index : " % num, str(r))
