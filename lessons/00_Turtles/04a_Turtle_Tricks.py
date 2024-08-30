"""
For this program, you will tell Tina the Turtle to draw 
a triangle.

You should look at the previous program, 02_Meet_Tina.py
to see how to use the turtle commands.


"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.forward(90) 
tina.forward(90)
tina.left(90)
# Make each side of the triangle a different color with 
tina.pencolor("red")
tina.pendown
tina.circle(100)
tina.isvisible
tina.forward(90)
tina.circle(150)
tina.shapesize(10)
tina.left(90)
tina.forward(400)
tina.begin_fill()
tina.circle(90)
tina.end_fill()
tina.right(180)
tina.forward(300)
tina.begin_fill()
tina.circle(170)
tina.end_fill()
tina.begin_fill()
tina.circle(3000)
tina.end_fill()
tina.right(90)
tina.forward(10)
tina.begin_fill()
tina.circle(2000)
tina.end_fill()
tina.forward(100)
tina.right(180)
turtle.exitonclick()                    # Close the window when we click on it
