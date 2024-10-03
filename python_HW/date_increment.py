def dateIncrement(d):
    month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 11: 30, 10: 31, 12: 31}
    y = int(d[-4::])
    if y % 400 == 0 or (y % 100 != 0 and y % 4 == 0):
        month[2] = 29
    m = int(d[3:5])
    day = int(d[:2])
    separator = d[2]
    if day < month[m]:
        day = day + 1
    else:
        day = 1
        if m < 12:
            m += 1
        else:
            m = 1
            y += 1
    dt = str(day) + separator + str(m) + separator + str(y)
    return dt


date = input("enter any date = ")
d1 = dateIncrement(date)
print(d1)

