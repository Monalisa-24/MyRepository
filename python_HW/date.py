month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 11: 30, 10: 31, 12: 31}
y = int(input("enter any year = "))
if y % 400 == 0 or (y % 100 != 0 and y % 4 == 0):
    month[2] = 29
m = int(input("enter any month = "))
print("number of days in month", m, "is = ", month[m])
