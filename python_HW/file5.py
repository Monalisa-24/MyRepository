import os
f = open("demofile4.txt", "r")
t = f.read()
print(t)
a = t.split()
b = " ".join(a)
f1 = open("temp.txt", "w")
f1.write(b)
f.close()
f1.close()
os.remove("demofile4.txt")
os.rename("temp.txt", "demofile4.txt")

