# 10% discount if the purchase amount exceeds 5000

p_amount = float(input("enter a amount : "))
disc = (p_amount * 10) / 100

npa = (p_amount - disc)
if p_amount > 5000:
    print("the net payable amount = ", npa)
else:
    print("the net payable amount = ", p_amount)
