"""
For this program, you will tell Tina the Turtle to draw 
a pentagon.

You should look at the previous program, 02_Meet_Tina.py
to see how to use the turtle commands.


"""


import turtle                           
turtle.setup (width=600, height=600)    
tina = turtle.Turtle()                  
tina.penup()
tina.right(90)
tina.forward(140)
tina.left(90)
tina.pendown()
tina.begin_fill()
tina.circle(220)
tina.end_fill()

tina.left(90)
tina.color('gold')
tina.forward(50)
tina.left(90)
tina.forward(97)
tina.right(90)
tina.forward(35)
tina.right(90)
tina.penup()
tina.forward(90)
tina.pendown()
tina.begin_fill()
tina.circle(175)
tina.end_fill()

tina.color('black')
tina.penup()
tina.goto(120,200)



















turtle.exitonclick()                    
