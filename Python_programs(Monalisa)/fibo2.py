def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return(fibo(n-1)+fibo(n-2))
no=int(input("enter the range : "))
for no in range(0,no):
    print(fibo(no))
