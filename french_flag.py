import turtle

# creating a new instance
flag = turtle.Turtle()

flag.speed(10)
flag.pensize(5)
flag.color('blue')
# Default background color is white which can be changed

def draw(x,y):
    flag.penup()
    flag.goto(x,y)
    flag.pendown()

draw(-150,0)
# Blue Rectangle
flag.color('blue')
flag.begin_fill()

flag.left(90)
flag.forward(400)
flag.left(90)
flag.forward(300)
flag.left(90)
flag.forward(800)
flag.left(90)
flag.forward(300)
flag.left(90)
flag.forward(400)

flag.end_fill()

draw(150,0)
# Red Rectangle
flag.color('red')
flag.begin_fill()


flag.forward(400)
flag.right(90)
flag.forward(300)
flag.right(90)
flag.forward(800)
flag.right(90)
flag.forward(300)
flag.right(90)
flag.forward(400)

flag.end_fill()

turtle.done()
