import turtle
import math
turtle.setup(800,800)
def drawSide():
    turtle.speed(0)
    turtle.right(10)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(55)
    for i in range(0,27):
        turtle.forward(3)
        turtle.right(10)
    turtle.forward(3)
    turtle.left(55)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(40)
    turtle.right(10)
def drawPiece(origin):
    w = 0
    turtle.tracer(0.5, 0.5)
    for i in range(0, 4):
        turtle.setheading(i * 90)
        turtle.penup()
        if i == 0:
            turtle.goto(origin)
            turtle.begin_fill()
        elif i == 1:
            turtle.goto(origin[0] + w, origin[1] - w)
        elif i == 2:
            turtle.goto(origin[0] + w, origin[1] - w)
        elif i == 3:
            turtle.goto(origin[0], origin[1])
        turtle.pendown()
        drawSide()
        if i == 0:
            w = turtle.xcor() - origin[0]
    turtle.end_fill()
    turtle.update()
    return w
turtle.pencolor("#294366")
turtle.pensize(3)
width = drawPiece((0,0))
turtle.clear()
turtle.fillcolor("#96b5dd")
turtle.bgcolor("#365782")
for x in range(0, math.ceil(800/width) + 2):
    for y in range(0, math.ceil(800/width) + 2):
        if y % 2 == x % 2:
            drawPiece((x*width-450, y*width-450))
