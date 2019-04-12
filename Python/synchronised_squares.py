import turtle
import math
def turtleSquares(iteration):
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    turtle.bgcolor("black")
    turtles = []
    for i in range(0, iteration):
        t = turtle.Turtle()
        t.penup()
        t.speed(0)
        t.color(colors[i % 6])
        t.pencolor(colors[i % 6])
        t.shape("turtle")
        t.pensize(2)
        if i % 2 == 0:
            t.goto(-200/(2**(i/2)),200/(2**(i/2)))
        else:
            t.goto(0,200/(2**((i-1)/2)))
            t.right(45)
        t.pendown()
        turtles.append(t)
    for x in range(0,4):
        for i in range(0,40):
            for t in turtles[1:]:
                t.forward((400/(math.sqrt(2) ** (turtles.index(t))))/40)
            turtles[0].forward(10)
        for t in turtles:
            t.right(90)
turtleSquares(10)
