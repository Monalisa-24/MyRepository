PI = 3.14


def circle(r):
    area = PI * r * r
    circumference = 2 * PI * r

    return area, circumference


radius = float(input(" enter any number to radius :- "))

print("The area and circumference =", (circle(radius)))
