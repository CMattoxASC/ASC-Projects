from Myro import *
init("sim")
penDown()

def drawAC():
    i = 0
    while i < 4:
        motors(.25,-1,2)
        i = i + 1
 
drawAC()

penUp()
turnBy(180)
forward (1,2)
turnBy(90)
penDown()

backward(1,2)
penUp()
forward(1,2)
turnBy(45)
penDown()
backward(1,2)
turnBy(105)
backward(1,2)
turnBy(215)
backward(1,2)
      
      