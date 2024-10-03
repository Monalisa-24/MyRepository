def bubbleSort(my_list):
    n = len(my_list)

    for i in range(0, n):
        for j in range(n - 1):
            if my_list[j] > my_list[j + 1]:
                temp = my_list[j]
                my_list[j] = my_list[j + 1]
                my_list[j + 1] = temp
    return my_list


the_list = []
num = int(input("enter the number of elements of the list : "))
for k in range(0, num):
    number = int(input("enter the number  %d elements :" % k))
    the_list.append(number)
print("Ok now the list is ready...", the_list)
print("the list after sorted : ", bubbleSort(the_list))
