import turtle
import random
  
# global colors
col = ['red', 'yellow', 'green', 'blue',
       'white', 'black', 'orange', 'pink']
  
# method to call on screen click
  
  
def fxn(x, y):
    global col
    ind = random.randint(0, 7)
      
    # set screen color randomly
    sc.bgcolor(col[ind])
  
# set screen
sc = turtle.Screen()
sc.setup(400, 300)
  
# call method on screen click
turtle.onscreenclick(fxn)

turtle.done()