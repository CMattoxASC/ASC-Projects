from random import *

xCoordinate = 0
yCoordinate = 0

def setup():
    size(1000, 1000)
    background(255, 255, 255)

def draw():

    if mousePressed:
        noStroke()
        ellipse(mouseX, mouseY, 55, 55)
        fill(randint(0,255),
        randint(0,255), randint(0,255))
        
        x = mouseX + randint(-25,25)
        y = mouseY + randint(-25,25)