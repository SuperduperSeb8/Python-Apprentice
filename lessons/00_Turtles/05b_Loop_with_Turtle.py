
"""
Turtles with a loop. 

This program has four identical lines of code to draw a square, 
but you know you can use a loop to make the program simpler. 

"""


import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(2)                           # Make the turtle move as fast, but not too fast. 
tina.color('yellow')
tina.begin_fill()
tina.forward(150)                       # Move tina forward by the forward distance
tina.left(90)                        # Turn tina left by the left turn

tina.forward(150)                       # Continue the last two steps three more times
tina.left(90)                           # to draw a square

tina.forward(150)
tina.left(90)

tina.forward(150)
tina.left(90)
tina.right(90)
tina.forward(35)
tina.left(90)
tina.forward(150)
tina.left(90)
tina.forward(35)
tina.right(180)
tina.forward(35)
tina.right(90)
tina.forward(15)
tina.left(90)
tina.forward(20)
tina.right(90)
tina.forward(20)
tina.right(90)
tina.forward(20)
tina.left(90)
tina.forward(110)
tina.left(180)
tina.forward(10)
tina.right(90)
tina.forward(20)
tina.left(90)
tina.forward(20)
tina.left(90)
tina.forward(20)

tina.left(180)
tina.forward(20)
tina.right(90)
tina.forward(10)
tina.left(90)

tina.forward(70)
tina.right(90)
tina.forward(20)
tina.right(90)
tina.forward(10)
tina.right(90)
tina.forward(20)

tina.left(90)
tina.forward(60)
tina.right(90)
tina.forward(10)
tina.left(90)

tina.forward(20)
tina.right(90)
tina.forward(80)
tina.right(90)
tina.forward(20)
tina.left(90)
tina.forward(10)
tina.right(90)
tina.forward(60)
tina.left(90)
tina.forward(20)
tina.right(90)
tina.forward(10)
tina.right(90)
tina.forward(20)

tina.right(90)
tina.forward(70)
tina.right(90)
tina.end_fill()
tina.penup()
tina.goto(90,20)
tina.color('brown')

tina.forward(40)
tina.begin_fill()
tina.circle(15)
tina.goto(50,40)
tina.circle(15)
tina.goto(10,84)
tina.circle(15)
tina.goto(80,13)
tina.circle(15)
tina.goto(30,30)
tina.goto(53,67)
tina.circle(15)
tina.goto(71,34)
tina.circle(15)
tina.end_fill()























turtle.exitonclick()                    # Close the window when we click on it

