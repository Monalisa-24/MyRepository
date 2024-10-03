def check_prime(n):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                print(n, "isn't a prime number.")
                break
        else:
            print(n, "is a prime number.")

    else:
        print(n, "isn't a prime number.")


a = int(input("enter any number to check :- "))
check_prime(a)
