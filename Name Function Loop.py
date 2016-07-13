from Myro import *
init("sim")
penDown()

def drawASquare():
    i = 0
    while i < 4:
        forward(1,1)
        turnBy(90)
        i = i +1
 
drawASquare()
      
      