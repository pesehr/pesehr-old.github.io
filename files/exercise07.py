import turtle
import math

WIDTH = 800
HEIGHT = 600
RATIO = 5

# setting up the screen
screen = turtle.getscreen()
screen.setup(WIDTH, HEIGHT, 0,0)
screen.setworldcoordinates(0,0, WIDTH, HEIGHT)
turtle.speed(90)


# Draw Y axis
turtle.penup()
turtle.goto(WIDTH / 2,0)
turtle.pendown()
turtle.goto(WIDTH / 2,HEIGHT)

# Draw X axis
turtle.penup()
turtle.goto(0,HEIGHT/2)
turtle.pendown()
turtle.goto(WIDTH,HEIGHT/2)

# X axis line ticks
#TODO

# Y axis line ticks
#TODO


turtle.exitonclick()