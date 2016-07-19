from time import *
from random import *
from math import sqrt
a = randrange(50,450)
b = randrange(50,450)
xCoordinate = a
yCoordinate = b
c = choice([-5, -3, 3, 5])
xSpeed = c
ySpeed = c

def setup():
    size(500, 500)
    background(255, 255, 255)
    
def draw():
    global xCoordinate 
    global yCoordinate
    global xSpeed
    global ySpeed
    
    background(255, 255, 255)
    fill(0, 0, 255)  
    ellipse(xCoordinate, yCoordinate, 50, 50)
    noStroke()
    xCoordinate = xCoordinate + xSpeed
    yCoordinate = yCoordinate + ySpeed 
    ellipse(xCoordinate, yCoordinate, 50, 50)
    
    if xCoordinate > 489:
        xSpeed = xSpeed *-1
    if yCoordinate > 489:    
        ySpeed = ySpeed*-1
    if xCoordinate < 20:
        xSpeed = xSpeed *-1
    if yCoordinate < 20:
        ySpeed = ySpeed*-1
            
                    
    
sleep(.01)