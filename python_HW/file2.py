f = open("demofile3.txt", "r")
a = int(input("enter the number of the lines = "))
for i in range(a):
    c = f.readline()
    print(c)
f.close()
