# telephone bill

p = int(input("Enter the number of calls : "))

if p <= 75:
    c = 250
    # print("charge = ", c)
elif p <= 150:
    c = float(250 + (p - 75) * 0.80)
    # print("charge = ", c)
elif p <= 225:
    c = float(250 + (p - 150) * 1.00 + 75 * 0.80)
    # print("charge = ", c)
else:
    c = float(250 + (p - 225) * 1.20 + 75 * 1.00 + 75 * 0.80)
print("charge = ", c)
