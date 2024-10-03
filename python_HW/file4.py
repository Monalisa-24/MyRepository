f = open("demofile3.txt", "r")
n = int(input("enter the string to find = "))
for i in range(n):
    t = f.readline()
    print(t)
f.close()
