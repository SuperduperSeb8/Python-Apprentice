
"""
Turtles with a loop. 

Study the previous program, 05a_Loop_with_Turtle.py, and then
write a new program that uses a loop to draw a pentagon.
( You can cut and past most of it! )

"""
import turtle
tina = turtle.Turtle()
tina.color ('yellow')
tina.begin_fill()
tina.circle(100)
tina.end_fill()
tina.color ('brown')
tina.shape("arrow")

tina.left(90)
tina.forward(40)
tina.left(90)

tina.begin_fill()
tina.forward(75)
tina.left(90)
tina.forward(40)
tina.left(90)
tina.forward(150)
tina.left(90)
tina.forward(40)
tina.left(90)
tina.forward(70)
tina.end_fill()

tina.penup()
tina.right(90)
tina.forward(90)
tina.left(90)
tina.forward(50)
tina.right(90)
tina.color('white')
tina.begin_fill()
tina.circle(15)
tina.end_fill()
tina.color('black')
tina.begin_fill()
tina.circle(9)
tina.end_fill()

tina.color('white')
tina.right(90)
tina.forward(90)
tina.right(90)
tina.forward(2)
tina.begin_fill()
tina.circle(15)
tina.end_fill()

tina.color('black')
tina.begin_fill()
tina.circle(9)
tina.end_fill()
tina.left(90)

tina.color('brown')
for i in ['a','b','c','d']:
    print(i)
for c in "Hello World!":
    print(c)
tina.goto


















turtle.exitonclick()