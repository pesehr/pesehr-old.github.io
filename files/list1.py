def check_set(list):
	for i in list:
		if list.count(i) > 1:
			return False
	return True

def intersections(list1, list2):
	intersection = [] 
	for i in list1:
		if i in list2:
			intersection.append(i)
	return intersection

def union(list1, list2):
	union = list1.copy()
	for i in list2:
		if i not in union:
			union.append(i)
	return union

list1 = (input("enter list 1")).split(",")
list2 = (input("emter list 2")).split(",")

if check_set(list1) and check_set(list2):
	print("intersections: ",intersections(list1,list2))
	print("union: ", union(list1,list2))
else:
	print("invalid set")

