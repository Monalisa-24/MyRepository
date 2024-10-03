s = input("enter any string : ")
w = s.split()
d = {}
for i in w:
    d[i] = d.get(i, 0) + 1
print(d)

