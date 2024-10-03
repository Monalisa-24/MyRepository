def sum_of_digit(a):
    if a != 0:
        return a % 10 + sum_of_digit(a // 10)
    else:
        return a


n = int(input("Enter any number :  "))
print("the sum of digits of these numbers : ", sum_of_digit(n))
