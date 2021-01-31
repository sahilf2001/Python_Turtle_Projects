#Turtle
'''parameters involved:
-->location
-->direction
-->a pen
'''

import turtle

# creating a new instance
flag = turtle.Turtle()

flag.speed(3)
flag.pensize(5)
flag.color('blue')
# Default background color is white which can be changed
# Ashoka chakra 360/24 = 15 degree

def draw(x,y):
    flag.penup()
    flag.goto(x,y)
    flag.pendown()
# Ashoka Chakra
for i in range(24):
    flag.forward(80)#length of each stroke
    flag.backward(80)
    flag.left(15)

draw(0,-80)
flag.circle(80,360)

# Green Rectangle
flag.color('green')
flag.begin_fill()

flag.forward(400)
flag.backward(800)
flag.right(90)
flag.forward(250)
flag.left(90)
flag.forward(800)
flag.left(90)
flag.forward(250)
flag.left(90)

flag.end_fill()

# Orange Rectangle
flag.color('orange')
draw(-400,80)
flag.begin_fill()

flag.right(90)
flag.forward(250)
flag.right(90)
flag.forward(800)
flag.right(90)
flag.forward(250)
flag.right(90)
flag.forward(800)

flag.end_fill()



turtle.done()
