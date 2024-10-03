f = open("demofile3.txt", "r")
a = f.read().split()
n = {}
for i in a:
    n[i] = n.get(i, 0) + 1
print(n)
f.close()
