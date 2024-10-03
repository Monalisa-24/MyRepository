'''def BubSort(list):
    l=len(list)
    for i in range(l-1,0,-1):
        for j in range(i):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
    print(list)
list1=[5,2,3,4,1,0]
BubSort(list1)

#-------------------------------'''

def SelecSort(list2):
    l=len(list2)
    for i in range(l-1):
        min=i
        for j in range(i+1,l):
            if list[j]<list[min]:
                min=j
        list[i],list[min]=list[min],list[i]

list2=[5,2,3,4,1,0]
SelecSort(list2)
print(list2)
        
