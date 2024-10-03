def marge_lists(my_list1, my_list2):
    for i in my_list2:
        my_list1.append(i)
    my_list1.sort()
    return my_list1


print("Here we've the two sorted lists to marge them....")
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_2 = [20, 21, 23, 40, 0, 18, 25, 30, 35]
print("the new list ....", marge_lists(list_1, list_2))
