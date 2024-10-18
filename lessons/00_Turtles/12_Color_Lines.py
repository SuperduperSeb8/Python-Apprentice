"""
Color Lines

1) Finish the program to make Tina draw a square with each side being a different color. 

"""

import turtle   
import random                         # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(2)                           # Make the turtle move as fast, but not too fast. 

tina.pendown()

tina.begin_fill()
tina.circle(150)
tina.left(90)
tina.forward(35)
tina.left(90)
tina.circle(110)
tina.forward(80)
tina.circle(100)
tina.left(180)
tina.forward(100)
tina.circle(100)
tina.left(180)
tina.circle(200)
tina.circle(500)
tina.left(180)
tina.circle(500)
tina.forward(90)
tina.left(90)
tina.circle(2000)
tina.goto(201,-12)
tina.circle(600)
tina.end_fill()
colors = [ 'red', 'blue', 'black', 'orange']    # define a list of colors

tina.color(random.choice(colors))                  # loop through the colors






















































































turtle.exitonclick()                     # Close the window when we click on it