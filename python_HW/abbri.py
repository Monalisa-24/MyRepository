name = input("enter any name : ")
name = name.strip()
print(name)
abbri = name[0]
print(abbri)
last = name.rfind(" ")
print(last)
i = 0
print(name[i])
print(name[i + 1])
while i < last:
    if name[i] == " " and name[i + 1] != " ":
        abbri += "." + name[i + 1]
    i += 1
abbri += "." + name[last + 1:]
print(abbri)
