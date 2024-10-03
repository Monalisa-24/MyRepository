def avg_number(a, b, c):
    total_number = a + b + c
    average = total_number / 3
    print("His/Her average number is = ", average)
    if 90 <= average <= 100:
        print("His/Her Grade is = A.")
        print("A stands for -> \033[1m EXCELLENT \033[0m, Promoted.")
    elif 80 <= average <= 89:
        print("His/Her Grade is = B.")
        print("B stands for -> \033[1m VERY GOOD \033[0m, Promoted.")
    elif 70 <= average <= 79:
        print("His/Her Grade is = C.")
        print("C stands for -> \033[1m GOOD \033[0m, Promoted.")
    elif 60 <= average <= 69:
        print("His/Her Grade is = D")
        print("D stands for -> \033[1m BAD \033[0m, Promoted with PERMISSION.")
    else:
        print("His/Her Grade is = F, Fail.")
        print("F stands for -> \033[1m FAIL \033[0m.")


Name = input("Name of the Candidate :-- ")
x = int(input("Number in Mathematics -> "))
y = int(input("Number in Python -> "))
z = int(input("Number in C.Architecture -> "))
avg_number(x, y, z)


