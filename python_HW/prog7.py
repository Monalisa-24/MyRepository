# courier company

w = float(input("enter the weight : "))
# r = 25

if w <= 20:
    total_charge = 25

else:
    next_part = w - 20
    times = next_part // 10
    rem = next_part % 10
    if rem != 0:
        times += 1
    total_charge = 25 + times * 5

print(" the charges = ", total_charge)
