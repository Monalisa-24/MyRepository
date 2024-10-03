# 10% discount if the purchase amount exceeds 5000 otherwise 5% discount

p_amount = float(input("enter a amount : "))
disc1 = (p_amount * 10) / 100
disc2 = (p_amount * 5) / 100

npa1 = (p_amount - disc1)
npa2 = (p_amount - disc2)

if p_amount > 5000:
    print("the net payable amount = ", npa1)
else:
    print("the net payable amount = ", npa2)
