from time import *
from random import *

ship = 200
bulletY = 450
isBulletFired = False
bulletX = 0
def setup():
    size(500,500)
    background(0)
    
    global aliens
    
    aliens = [[1, 1, 1, 1, 1], 
    [1, 1, 1, 1, 1], 
    [1, 1, 1, 1, 1], 
    [1, 1, 1, 1, 1]]
    
 

def draw():
    global xAlien
    global yAlien
    global ship
    global isBulletFired
    global bulletY
    global bulletX
    xAlien = 50
    yAlien = 50
    sleep(0.0001)
    mX = mouseX
    background(255)
    rect(ship, 450, 100,20)
    fill(0)

    #print(ship)
    
    #THIS MAKES THE SPACE SHIP MOVE
    if keyPressed:
        if key == 'k' and ship > 0:
            ship = ship - 10
        if key == 'l' and ship < 400:
            ship = ship + 10    
        if key == 'j':
            isBulletFired = True
    
    #SHOOTS BULLET
    if isBulletFired == True:
        if bulletY < 0:
            isBulletFired = False
            bulletY = 450
        else:
            fill(255,0,0)
            ellipse(ship + 50,bulletY,10,10)
            bulletY = bulletY - 20

        
    if isBulletFired == True:
        row = 0
        column = 0
        while row < 4:
            while column < 5:
                if bulletX > (xAlien - 25) and bulletX < xAlien + 25 and bulletY < yAlien + 25:
                    isBulletFired = False
                    bulletY = 450
                    aliens [bulletY// 100] [bulletX // 100] = 0
                xAlien = xAlien + 100
            yAlien = yAlien + 100
            
                                
                                        
                                                
                                                        
                                                                
                                                                                                
        # if bulletY < 250: #MAKING THE ALIENS DISAPPEAR
        #     if bulletX < 70:
        #         if bulletx > 50:
        #             print("lol")
    
    # row = 3
    # column = 4   
    #    #Make Circles Disappear         
    # while row > 0:
    #     while column > 0:
    #         if bulletX > xAlien - 75 and bulletX < xAlien + 75 and isBulletFired == True and bulletY < yAlien + 30:
    #             print ("i shot an alien")
    #             isBulletFired = False
    #             aliens[bulletY // 100][bulletX // 100] = 0
    #             print (aliens)
    #         xAlien = xAlien - 100
    #         column = column - 1
    #     xAlien = 450
    #     yAlien -= 70   
    #     row = row - 1
        
    # xAlien = 50
    # yAlien = 20
     
       #DRAWS THE ALIENS
    for row in aliens:
        for alienIndex in row:
            if alienIndex == 1:
                fill(0)
                ellipse(xAlien, yAlien, 50, 50)
                xAlien = xAlien + 100
            elif alienIndex == 0:
                xAlien = xAlien + 50
        xAlien = 50
        yAlien += 70