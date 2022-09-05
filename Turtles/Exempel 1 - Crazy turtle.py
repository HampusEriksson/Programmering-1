import turtle, random

adam = turtle.Turtle()
adam.pensize(3)
adam.shapesize(1)
adam.hideturtle()

while True:
    adam.right(random.randint(1,15))
    adam.forward(random.randint(10,30))
    adam.color(random.random(), random.random(), random.random())

    if abs(adam.xcor()) > 400 or abs(adam.ycor()) > 400:
        adam.penup()
        adam.goto(0,0)
        adam.pendown()

turtle.done()