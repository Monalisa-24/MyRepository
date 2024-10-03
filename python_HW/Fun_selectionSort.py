def selectionSort(my_list):
    n = len(my_list)

    for i in range(0, n):
        min_ele = i
        for j in range(i + 1, n):
            if my_list[j] < my_list[min_ele]:
                min_ele = j
        my_list[i], my_list[min_ele] = my_list[min_ele], my_list[i]
    return my_list


the_list = []
num = int(input("enter the number of elements of the list : "))
for k in range(0, num):
    number = int(input("enter the number  %d elements :" % k))
    the_list.append(number)
print("Ok now the list is ready...", the_list)
print("the list after sorted : ", selectionSort(the_list))
