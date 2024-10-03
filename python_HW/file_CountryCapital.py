import os
f = open("demofile6.txt", "r")
r = f.read()
s = r.split("\n")
d1 = {}
for i in r:
    if len(i) == 0:
        break
    l = i.split(":")
    d1[l[0]] = l[l]
f.close()
while True:
    print("<...........................................>")
    print("Press 1 for add.")
    print("Press 2 for delete.")
    print("Press 3 for update.")
    print("Press 4 for search.")
    print("Press 5 for exit.")
    print("<...........................................>")
    n = int(input("Enter your choice :- "))
    if n == 1:
        key = input("Country Name")
        d1[key] = input("Capital Name")
    elif n == 2:
        key = input("Country Name")
        d1.pop(key)
    elif n == 3 :
        key = input("Country Name")
        value = input("Capital Name")
        d1[key] = value
    elif n == 4:
        key = input("Country Name")
        if key in d1:
            print("Capital of ", key, "is", d1[key])
        else:
            print("Can't be found.")

    elif n == 5:
        break
    else:
        print("Invalid Choice.")

int(d1)
f1 = open("demofile7.txt", "w")
for k, v in d1.items():
    f1.write(k+":"+v+"\n")
f1.close()
os.remove("demofile6.txt")
os.rename("demofile7.txt", "demofile6.txt")





