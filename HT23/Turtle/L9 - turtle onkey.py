# Importerar turtle
import turtle, random

# Create a Turtle screen
screen = turtle.Screen()
screen.bgcolor("blue")

# Skapar en turtle
fares = turtle.Turtle()
fares.penup()
fares.shapesize(3)

batin = turtle.Turtle()
batin.color("red")
batin.shapesize(3)
batin.penup()

# Skapar en funktion för space
def up():
    fares.seth(90)
    fares.forward(20)
    # skulle också kunna skriva:
    # fares.sety(fares.ycor() + 20)

def down():
    fares.seth(270)
    fares.forward(20)

def right():
    fares.seth(0)
    fares.forward(20)

def left():
    fares.seth(180)
    fares.forward(20)
      
def click(x,y):
    fares.goto(x,y)
    

# Säger att funktionen space ska användas när space klickas
screen.onkey(up,'Up')
screen.onkey(down,"Down")
screen.onkey(right,'Right')
screen.onkey(left,'Left')

# Säger att funktionen click ska användas när space klickas
screen.onscreenclick(click)

screen.listen()

# Skapar en loop som gör att skärmen inte stängs
while True:
    if fares.distance(batin) < 50:
        batin.goto(random.randint(-400,400), random.randint(-400,400))
    elif fares.distance(batin) < 20:
        batin.goto(random.randint(-400,400), random.randint(-400,400))
    else:
        fares.forward(1)

      
    screen.update()
        