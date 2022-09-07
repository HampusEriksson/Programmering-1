# Importerar turtle
import turtle

# Skapar en turtle
adam = turtle.Turtle()

# Skapar en funktion för space
def space():
    adam.forward(20)
      
def click(x,y):
    adam.goto(x,y)
    
# Säger att funktionen space ska användas när space klickas
turtle.onkey(space,'space')

# Säger att funktionen click ska användas när space klickas
turtle.onscreenclick(click)

turtle.listen()

turtle.mainloop()