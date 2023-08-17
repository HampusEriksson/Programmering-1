import turtle, random

benny = turtle.Turtle()
benny.shapesize(10)

benny.forward(random.randint(50,200))

benny.color(random.random(), random.random(), random.random())

colors = ["red", "green"]

benny.color(random.choice(colors))

turtle.done()