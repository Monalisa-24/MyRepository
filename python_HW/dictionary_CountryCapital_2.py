while True:
    print("Enter 1 to add.")
    print("Enter 2 to edit.")
    print("Enter 3 to search.")
    print("Enter 4 to delete.")
    print("Enter 0 to exit.")
    choice = int(input("Enter your choice - "))
    d = {}


    def add():
        n = int(input("enter the number of countries - "))
        for i in range(n):
            k = input("enter the country name - ")
            d[k] = input("enter the capital name - ")
        return d


    def edit():
        cn = input("enter the country name - ")
        if cn in d.keys():
            d[cn] = input("new capital - ")
        return d


    def search():
        cn = input("enter the country name - ")
        if cn in d.keys():
            print("Search Successful.")
        else:
            print("Search Unsuccessful.")


    def delete():
        cn = input("enter the country name you want to delete - ")
        if cn in d.keys():
            d.pop(cn)
        return d


    if choice == 1:
        print(add())
    if choice == 2:
        print(edit())
    if choice == 3:
        search()
    if choice == 4:
        print(delete())
    if choice == 0:
        break
