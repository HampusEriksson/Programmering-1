# Importerar turtle
import turtle, random, time

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
turtle.onkey(up,'Up')
turtle.onkey(down,'Down')
turtle.onkey(right,'Right')
turtle.onkey(left,'Left')

# Säger att funktionen click ska användas när space klickas
# turtle.onscreenclick(click)

turtle.listen()

while True:
    dis = ((fares.xcor()-batin.xcor())**2 + (fares.ycor()-batin.ycor())**2)**0.5
    if dis < 50:
        batin.goto(random.randint(-400,400), random.randint(-400,400))
        
turtle.mainloop()