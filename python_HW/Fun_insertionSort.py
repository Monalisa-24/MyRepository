def insertionSort(my_list):
    n = len(my_list)

    for i in range(0, n):
        temp = my_list[i]
        j = i - 1
        while temp < my_list[j] and j >= 0:
            my_list[j + 1] = my_list[j]
            j = j - 1
        my_list[j + 1] = temp
    return my_list


the_list = []
num = int(input("enter the number of elements of the list : "))
for k in range(0, num):
    number = int(input("enter the number  %d elements :" % k))
    the_list.append(number)
print("Ok now the list is ready...", the_list)
print("the list after sorted : ", insertionSort(the_list))
