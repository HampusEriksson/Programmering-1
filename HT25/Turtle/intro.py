# För att använda turtle måste modulen importeras
import turtle, random
# Skapa en turtle
padda = turtle.Turtle()
kalle = turtle.Turtle()
# Ändra på turtle
# Shape - "arrow", "turtle", "circle", "square", "triangle", "classic"
padda.shape("turtle")
kalle.shape("arrow")
# Shapesize, pensize
padda.shapesize(5)
kalle.shapesize(2)
# Speed - 1 till 10, men 0 är snabbast
padda.speed(5)
# Röra på turtle - .forward, .back, .goto, .setx, .sety
kalle.forward(300)
# Penup, pendown
padda.goto(200, 100)
padda.penup()
padda.forward(200)
# Sluta rita - .penup
# Börja rita igen - .pendown
# Byt med text - .pencolor
kalle.pencolor("red")
kalle.color("red")
kalle.goto(-300, -300)
# Rotera - .right, .left, .seth
kalle.right(90)
kalle.forward(300)
# Byt med rgb
# .hideturtle(), .showturtle()

# Circle (radie, vinkel, streck)
padda.pendown()
padda.circle(50)
padda.circle(200)

# Dot (storlek, färg)
# Få data från turtle .pos, .xcor, .ycor, .heading
# Distance (a,b)
# Skriv turtle.done() för att fönstret ska vara kvar öppet


padda.goto(0,0)

padda.speed(0)
for i in range(1000):
    padda.right(i*10)
    padda.forward(50)
    padda.color(random.random(), random.random(), random.random())
turtle.done()