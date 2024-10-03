# Function to take multiple arguments
def add(int, *args):
    answer=0
    for i in args:
        answer=answer+i
    print(answer)


def add(str, *args):
    answer=''
    for i in args:
        answer=answer+i
    return answer

	


# Integer
#add('int', 5, 6) // this will throw an error

# String
print(add('str', 'Hi ', 'Geeks'))
