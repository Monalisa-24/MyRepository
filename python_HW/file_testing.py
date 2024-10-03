f = open("demofile1.txt", "rb")
print(f.readline())
print(f.readline())
print("\n")

file = open("F:\\python_HW\demofile2.txt", "r")
print(file.read())
print("\n")

f = open("demofile1.txt", "a")
# f.write("Hope you get your success very soon...!")
f.close()
f = open("demofile1.txt", "rt")
print(f.read())
f.close()

# f = open("demofile4.txt", "x")
f = open("demofile6.txt", "w")

import os
# os.remove("demofile5.txt")

f = open("demofile3.txt", "w")

if os.path.exists("demofile4.txt"):
    os.remove("demofile4.txt")
else:
    print("The file doesn't exist !!!")

# os.rmdir("F:\\python3\demofilessssss")
