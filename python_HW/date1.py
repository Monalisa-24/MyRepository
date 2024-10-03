month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 11: 30, 10: 31, 12: 31}
d = input("enter any date : ")
y = int(d[-4::])
print(y)
if y % 400 == 0 or (y % 100 != 0 and y % 4 == 0):
    month[2] = 29
m = int(d[3:5])
day = int(d[:2])
print(m, day)
print("number of days in month", m, "is", month[m])
