def linearSearch(the_list, x):
    for i in range(len(the_list)):
        if the_list[i] == x:
            return i

    return -1


my_list = []
n = int(input("enter the number of elements of the list : "))
for j in range(0, n):
    number = int(input("enter the number  %d elements :" % j))
    my_list.append(number)
print("now the list is = ", my_list)

num = int(input("Enter the number for searching : "))
print("The Output Is = ", linearSearch(my_list, num))
