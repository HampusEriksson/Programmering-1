import turtle, random

adam = turtle.Turtle()
adam.pensize(5)
adam.shapesize(0.1)
adam.showturtle()
adam.speed(0)

while True:
    adam.right(random.randint(1,15))
    adam.forward(random.randint(10,30))
    adam.color(random.random(), random.random(), random.random())
    adam.dot(25, (random.random(),random.random(),random.random()))

    if abs(adam.xcor()) > 400 or abs(adam.ycor()) > 400:
        adam.penup()
        adam.goto(0,0)
        adam.pendown()
        

turtle.done()