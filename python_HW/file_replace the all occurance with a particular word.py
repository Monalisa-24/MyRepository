f = open("demofile2.txt", "r")
r = f.read()
n = input("Enter the word which you want to replace - ")
nn = input("Enter the word by which you want to replace - ")
replace = r.replace(n, nn)
print(r)
print(replace)
f.close()
f1 = open("demofile2.txt", "w")
f1.write(replace)
f1.close()
