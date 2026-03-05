import turtle

# Inställningar
screen = turtle.Screen()
screen.setup(width=800, height=600)
padda = turtle.Turtle()
padda.speed(0)
riktning = "up"

# Turtle för score
score_turtle = turtle.Turtle()
score_turtle.hideturtle()
score_turtle.penup()
score_turtle.goto(-350, 350)
score_turtle.color("black")

score = 0

def uppdatera_score():
    global score
    score += 1
    score_turtle.clear()
    score_turtle.write(f"Score: {score}", font=("Arial", 24, "normal"))

# Funktioner som bara ändrar variabeln 'riktning'
def ga_upp():
    padda.seth(90)

def ga_ner():
    padda.seth(270)

def ga_vanster():
   padda.seth(180)

def ga_hoger():
    padda.seth(0)

# Koppla tangenter
screen.listen()
screen.onkeypress(ga_upp, "Up")
screen.onkeypress(ga_ner, "Down")
screen.onkeypress(ga_vanster, "Left")
screen.onkeypress(ga_hoger, "Right")

# Huvudloopen som sköter rörelsen
def flytta():
   
    padda.forward(5)
    
    # Kör denna funktion igen efter 20 millisekunder
    screen.ontimer(flytta, 20)

flytta() # Starta rörelsen
screen.mainloop()