# För att använda turtle måste modulen importeras
import turtle

# Skapa en turtle
padda = turtle.Turtle()

# Ändra på turtle
# Shape - “arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”
padda.shape("turtle")

# Shapesize, pensize
padda.shapesize(7)
padda.pensize(7)

# Speed - 1 till 10, men 0 är snabbast
padda.speed(0)

# Röra på turtle - .forward, .back, .goto, .setx, .sety
padda.forward(50)
padda.back(100)
padda.goto(250, - 150)

# Penup, pendown,
# Sluta rita - .penup
padda.penup()


# Börja rita igen - .pendown
padda.pendown()


# Byt med text - .pencolor
padda.pencolor("red")
padda.goto(-250, 100)

# Byt med rgb

# .hideturtle(), .showturtle()
padda.hideturtle()
padda.showturtle()

# Rotera - .right, .left, .seth
padda.right(90)
padda.left(75)
padda.seth(180)

# Circle (radie, vinkel, streck)
padda.circle(400)
padda.circle(100, 360, 4)

# Dot (storlek, färg)
padda.dot(300, "yellow")

# Få data från turtle .pos, .xcor, .ycor, .heading
print(padda.pos())
padda.xcor()

if abs(padda.xcor()) > 400 or abs(padda.ycor()) > 400:
    padda.goto(0,0)

# Distance (a,b)
krokodil = turtle.Turtle()

if padda.distance(krokodil) < 10:
    print("Oj vad de är nära varandra")

# Skriv turtle.done() för att fönstret ska vara kvar öppet
turtle.done()
