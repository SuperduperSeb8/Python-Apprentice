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
tina.left(90)                # Close the window when we click on it
tina.circle(100)
tina.left(100)
tina.goto(-200,200)
tina.goto(-100,100)
tina.goto(0,0)
tina.begin_fill()
tina.circle(200)
tina.end_fill()











turtle.exitonclick()                                                     