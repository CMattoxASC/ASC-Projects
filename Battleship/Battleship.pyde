from random import *
x = 0 
y = 0
i = 0
def setup():
    size(600, 600)

    global board

    board = [[0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0]]     

    board[randrange(6)][randrange(6)] = 1
'''
if mousePressed: = 1:
    if mouseX < 100 and mouseY < 100:
        board[0][0]
    if mouseX < 200 and mouseY < 100:
        board[0][1]
    if mouseX < 300 and mouseY < 100:    
        board[0][2]
    if mouseX < 400 and mouseY < 100:
        board[0][3]
    if mouseX < 500 and mouseY < 100:
        board[0][4]
    if mouseX < 600 and mouseY < 100:            
            board[0][5]
            
    if mouseX < 100 and mouseY < 200:
    board[1][0]
    if mouseX < 200 and mouseY < 200:
    board[1][1]
    if mouseX < 300 and mouseY < 200:
    board[1][2]
    if mouseX < 400 and mouseY < 200:
    board[1][3]
    if mouseX < 500 and mouseY < 200:
    board[1][4]
    if mouseX < 600 and mouseY < 200:                
    board[1][5]        
            
    if mouseX < 100 and mouseY < 300:            
    board[2][0]
    if mouseX < 200 and mouseY < 300:
    board[2][0]
    if mouseX < 300 and mouseY < 300:
    board[2][0]
    if mouseX < 400 and mouseY < 300:
    board[2][0]
    if mouseX < 500 and mouseY < 300:
    board[2][0]
    if mouseX < 600 and mouseY < 300: 
    board[2][0]
    
    if mouseX < 100 and mouseY < 400:        
    board[3][0]
    if mouseX < 200 and mouseY < 400:
    board[3][1]
    if mouseX < 300 and mouseY < 400:
    board[3][2]
    if mouseX < 400 and mouseY < 400:
    board[3][3]
    if mouseX < 500 and mouseY < 400:
    board[3][4]
    if mouseX < 600 and mouseY < 400:  
    board[3][5]
            
    if mouseX < 100 and mouseY < 500:                                    
    board[4][0]
    if mouseX < 200 and mouseY < 500:
    board[4][1]
    if mouseX < 300 and mouseY < 500:
    board[4][2]
    if mouseX < 400 and mouseY < 500:
    board[4][3]
    if mouseX < 500 and mouseY < 500:
    board[4][4]
    if mouseX < 600 and mouseY < 500:        
    board[4][5]  
          
    if mouseX < 100 and mouseY < 600: 
    
    if mouseX < 200 and mouseY < 600: 
    
    if mouseX < 300 and mouseY < 600: 
    
    if mouseX < 400 and mouseY < 600: 
    
    if mouseX < 500 and mouseY < 600: 
    
    if mouseX < 600 and mouseY < 600: 
            
            
            print("You Win!)
'''

def draw():
    global i
    global x
    global y 
    while i < 6:
        fill(255, 0, 0)
        rect(x, y, 100, 100)
        i = i + 1
        fill(0, 0, 255)
        x = x + 100
        
    x = 0
    y = 100    
    
    while i < 12:
        fill(255, 255, 255)
        rect(x, y, 100, 100)
        i = i + 1
        fill(0, 0, 255)
        x = x + 100
        
    x = 0
    y = 200
  
    while i < 18:
        fill(0, 0, 255)
        rect(x, y, 100, 100)
        i = i + 1
        fill(0, 0, 255)
        x = x + 100
        
    x = 0
    y = 300
    
    while i < 24:
        fill(255, 0, 0)
        rect(x, y, 100, 100)
        i = i + 1
        fill(0, 0, 255)
        x = x + 100        
        
    x = 0
    y = 400
    
    while i < 30:
        fill(255, 255, 255)
        rect(x, y, 100, 100)
        i = i + 1
        fill(0, 0, 255)
        x = x + 100        
        
    x = 0
    y = 500
    
    while i < 36:
        fill(0, 0, 255)
        rect(x, y, 100, 100)
        i = i + 1
        fill(0, 0, 255)
        x = x + 100
    
    
"""
board = [[0, 0, 0, 0, 0, 0],
         
         [0, 0, 0, 0, 0, 0],
         
         [0, 0, 0, 0, 0, 0],
         
         [0, 0, 0, 0, 0, 0],
         
         [0, 0, 0, 0, 0, 0],
         
         [0, 0, 0, 0, 0, 0]]     


board[randrange(5)][randrange(5)] 
"""