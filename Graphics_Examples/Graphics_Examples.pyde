xCoordinate = 0

def setup ():
    size(500, 500)
    background(255, 255, 255)
    
    def draw():
        global xCoordinate
        
        background(255, 255, 255)
        fill(0, 0, 255)
        stroke(0, 0, 255)
        rect(xCoordinate, 250, 50, 50)
        fill(255, 0, 0)
        rect(150, 150, 25, 25)
        xCoordinate = xCoordinate + 1