n = int(input("enter any number = "))
t = n
r = 0

while n > 0:
    d = n % 10
    r = r *10 + d
    n = n // 10

if t == r:
    print("the number is palindrome.....")
else:
    print("the number is  not palindrome.....")