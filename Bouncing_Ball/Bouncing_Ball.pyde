from time import *
from random import *
from math import sqrt

xCoordinate = 250
yCoordinate = 250

xSpeed = 5
ySpeed = 5

def setup():
    size(500, 500)
    background(255, 255, 255)
    
def draw():
    global xCoordinate 
    global yCoordinate
    
    background(255, 255, 255)
    
    fill(0, 0, 255)  
    ellipse(xCoordinate, yCoordinate, 50, 50)
    
    noStroke()
    
    sleep(.01)
    
    if xCoordinate < 500 and yCoordinate < 500:
       xCoordinate = xCoordinate + xSpeed
       yCoordinate = yCoordinate + ySpeed
        
    if xCoordinate > 499 and yCoordinate > 499:
        xSpeed = xSpeed *-1
        ySpeed = ySpeed*-1
    
    

    
sleep(.01)