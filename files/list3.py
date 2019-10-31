import math
list = (input("enter a list: ")).split(",")

c_size = math.ceil(len(list) / 3)


for i in range(3):
    print(list[i*c_size:(i+1)*c_size])
