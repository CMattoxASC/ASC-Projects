from random import *

xCoordinate = 0
yCoordinate = 0

def setup():
    size(1000, 1000)
    background(255, 255, 255)    
    fill(255, 0, 0) 
    rect(0, 0, 200, 100)
    fill(0, 255, 0)
    rect(200, 0, 200, 100)
    fill(0, 0, 255)
    rect(400, 0, 200, 100)
    fill(0, 0, 0)
    rect(600, 0, 200, 100)
    fill(255, 255, 255)
    rect(800, 0, 200, 100)

def draw():

if mousePressed < 200:
    noStroke()
    ellipse(mouseX, mouseY, 15, 15)
    fill(255, 0, 0)    
if mousePressed < 400:
    noStroke()
    ellipse(mouseX, mouseY, 15, 15)
    fill(0, 255, 0)    
if mousePressed < 600:
    noStroke()
    ellipse(mouseX, mouseY, 15, 15)
    fill(0, 0, 255)
if mousePressed < 800:
    noStroke()
    ellipse(mouseX, mouseY, 15, 15)
    fill(0, 255, 0)
    elif mousePressed < 1000



    