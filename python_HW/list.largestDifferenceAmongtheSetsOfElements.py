def largeDiff(list1, n):
    large_diff = list1[1] - list1[0]

    for i in range(0, n):
        for j in range(0, n):
            if list1[j] - list1[i] > large_diff:
                large_diff = list1[j] - list1[i]

    return large_diff


array = [45, 23, 76, 15, 99, 43]
size = len(array)
print("Largest Difference = ", largeDiff(array, size))
