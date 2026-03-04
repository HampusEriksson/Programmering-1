import turtle, random
padda = turtle.Turtle()
turtle.screensize(1920,1080)
padda.speed(10)
padda.shape("turtle")
i = 0
while True:
    i += 1
    padda.goto(random.randint(-300, 300), random.randint(-300, 300))
    padda.color(random.random(), random.random(), random.random())
turtle.done()