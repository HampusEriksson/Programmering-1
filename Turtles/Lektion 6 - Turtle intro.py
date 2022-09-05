# För att använda turtle måste modulen importeras
import turtle

# Skapa en turtle
adam = turtle.Turtle()

# Ändra på turtle
# Speed - 1 till 10, men 0 är snabbast
adam.speed(0)

# Shape - “arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”
adam.shape("turtle")
"""
# Shapesize, pensize
adam.shapesize(5)
adam.pensize(5)
adam.forward(100)

# Röra på turtle - forward, back, goto, setx, sety
adam.forward(100)
adam.back(50)
adam.goto(-350,350)
adam.sety(-150)

# Penup, pendown, pencolor
# Sluta rita
adam.penup()

# Börja rita igen
adam.pendown()
# Byt med text
adam.pencolor("red")

# Byt med rgb
adam.pencolor(1, 0, 0)
adam.forward(100)

# Hideturtle, showturtle
adam.hideturtle()
adam.showturtle()

# Rotera - right, left, seth
adam.right(90)
adam.seth(132)

# Circle (radie, vinkel, streck)
adam.circle(75)

adam.circle(125, 180)

adam.circle(200, 270, 15)

# Dot (storlek, färg)
adam.dot(100, "black")

# Få data från turtle . pos, xcor, ycor, heading
adam.setx(500)
if adam.xcor() > 400:
    adam.setx(0)

adam.pos()
adam.ycor()
adam.heading()

# Distance (a,b)
harry = turtle.Turtle()
harry.shape("turtle")
harry.shapesize(5)
harry.pensize(5)
harry.goto(100, 150)

print(turtle.distance(adam, harry))
"""
while True:
    adam.right(7)
    adam.forward(50)
    if abs(adam.xcor()) > 400 or abs(adam.ycor()) > 400:
        adam.goto(0,0)

# Skriv turtle.done() för att fönstret ska vara kvar öppet
turtle.done()
