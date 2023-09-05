import turtle
import random

# Set up the Turtle screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a Turtle object
pen = turtle.Turtle()
pen.speed(0)

# Infinite loop to create the crazy pattern
while True:
    # Set a random pen color
    pen.color(random.random(), random.random(), random.random())

    # Set random starting position
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    pen.penup()
    pen.goto(x, y)
    pen.pendown()

    # Draw a random number of random line segments
    num_segments = random.randint(5, 15)
    for _ in range(num_segments):
        angle = random.randint(0, 360)
        length = random.randint(10, 100)
        pen.setheading(angle)
        pen.forward(length)

# Close the Turtle graphics window when done
turtle.done()
