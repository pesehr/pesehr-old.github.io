import turtle
import math


radios = int(input("Please enter radios:\n"))

#Calculate the circle area
area = math.pi * (radios ** 2)
print("Area: ",area)

#Draw the circle
turtle.circle(radios)

turtle.done()
