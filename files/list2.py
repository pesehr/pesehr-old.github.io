def sublist(list1, list2):
    for i in list2:
        if i not in list1:
            return False
    return True

list1 = (input("enter list 1: ")).split(",")
list2 = (input("enter list 2: ")).split(",")

print(sublist(list1,list2))

