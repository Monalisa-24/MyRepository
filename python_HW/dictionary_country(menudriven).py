country_capitals = {
    "India": "New Delhi",
    "Afghanistan": "Kabul",
    "Bangladesh": "Dhaka",
    "Japan": "Tokyo",
    "Bhutan": "Thimphu",
    "China": "beijing"
}
print(country_capitals)


def add_item():
    a = input("enter any country to key :- ")
    b = input("enter the capital to value :- ")
    country_capitals[a] = b
    print(country_capitals)


def remove_item():
    a = input("enter any country :- ")
    c = country_capitals.pop(a)
    print("popped element = ", c)
    print(country_capitals)


def update_item():
    a = input("enter any country :- ")
    b = input("enter the capital :- ")
    country_capitals[a] = b
    print(country_capitals)


def search():
    a = input("enter any country/capital :- ")
    if a in country_capitals.values():
        print("Searching is Successful.")
        key = list(country_capitals.keys())
        value = list(country_capitals.values())
        position = value.index(a)
        print("Capital = " + a + "\n" + " and " + "\n" + "Country = " + key[position])
    elif a in country_capitals.keys():
        print("Searching is Successful.")
        key = list(country_capitals.keys())
        value = list(country_capitals.values())
        position = key.index(a)
        print("Country = " + a + "\n" + " and " + "\n" + "Capital = " + value[position])
    else:
        print("Searching is Unsuccessful.")


while True:
    print("\n-----:MAIN MENU:-----")
    print("1. Add item")
    print("2. Remove item")
    print("3. Update item")
    print("4. Search item")
    choice = int(input("Enter the Choice:"))
    print(".....BE CAREFUL,TO AVOID ERRORS WRITE DOWN THE KEY-VALUES AS SAME AS IN THE DICTIONARY.....")

    if choice == 1:
        add_item()
    elif choice == 2:
        remove_item()
    elif choice == 3:
        update_item()
    elif choice == 4:
        search()
    else:
        print("oops!...please keep your choices between 1 - 4")
        break
