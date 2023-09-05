import turtle, random

benny = turtle.Turtle()
benny.shapesize(5)
benny.shape("turtle")

benny.forward(random.randint(50, 200))

benny.color(random.random(), random.random(), random.random())

colors = ["red", "green"]

benny.color(random.choice(colors))

while True:
    benny.circle(100)
turtle.done()
