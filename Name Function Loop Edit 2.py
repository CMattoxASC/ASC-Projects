from Myro import *
init("sim")
penDown()

def drawASquare():
    i = 0
    while i < 4:
        motors(.25,-1,2)
        i = i + 1
 
drawASquare()
      
      