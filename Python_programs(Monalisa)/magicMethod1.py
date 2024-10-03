class SetItemExample:
    def __init__(self, item):
        self.item = item
    def __setitem__(self, index, item1):
        self.item[index] = item1
setitem_instance = SetItemExample([1, 2, 3])
print(f"Items before setting: {setitem_instance.item}")
setitem_instance[1] = 5
print("Items after setting: ",setitem_instance.item)
# Output
# Items before setting: [1, 2, 3]
# Items after setting: [1, 5, 3]

#-----------------
class A:
    def __init__(self, item):
        self.item = item
    def __getitem__(self, index):
        return self.item[index]
a = A([1, 2, 3])
print(f"First item: {a[0]}")
print(f"Second item: {a[1]}")
print("Third item: ",a[2])
# Output: 
# First item: 1
# Second item: 2
# Third item: 3
