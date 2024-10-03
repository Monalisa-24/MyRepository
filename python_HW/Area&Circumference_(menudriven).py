def peri_triangle(a, b, c):
    perimeter = a + b + c
    print("The perimeter of Triangle =", perimeter, "cm")


def area_triangle(h, b):
    area = (h * b) / 2
    decimals = 2
    print("The area of Triangle = {0:.{1}f}cm\u00b2 ".format(area, decimals))


def peri_rectangle(le, w):
    perimeter = 2 * (le + w)
    print("The perimeter of Rectangle =", perimeter, "cm")


def area_rectangle(le, w):
    area = w * le
    decimals = 2
    print("The area of Rectangle = {0:.{1}f}cm\u00b2 ".format(area, decimals))


while True:
    print("-*-*-|MAIN MENU|-*-*-")
    print("1.Perimeter")
    print("2.Area")
    print("3.Exit")
    choice1 = int(input("Enter your first choice -> "))

    if choice1 == 1:
        print("\n***|CALCULATE PERIMETER|***")
        print("1.Triangle")
        print("2.Rectangle")
        print("3.Exit")
        choice2 = int(input("Enter your first choice -> "))

        if choice2 == 1:
            m = float(input("enter the first side = "))
            n = float(input("enter the second side = "))
            o = float(input("enter the third side = "))
            peri_triangle(m, n, o)
        elif choice2 == 2:
            length = float(input("enter the length = "))
            width = float(input("enter the width = "))
            peri_rectangle(length, width)
        elif choice2 == 3:
            break
        else:
            print("Ohho..! * Incorrect Option...|")

    elif choice1 == 2:
        print("\n***|CALCULATE AREA|***")
        print("1.Triangle")
        print("2.Rectangle")
        print("3.Exit")
        choice3 = int(input("Enter your first choice -> "))

        if choice3 == 1:
            base = float(input("enter the base = "))
            height = float(input("enter the height = "))
            area_triangle(base, height)
        elif choice3 == 2:
            length = float(input("enter the length = "))
            width = float(input("enter the width = "))
            area_rectangle(length, width)
        elif choice3 == 3:
            break
        else:
            print("Ohho..! * Incorrect Option...*")

    elif choice1 == 3:
        break
    else:
        print("Ohho..! * Incorrect Option...>>")



