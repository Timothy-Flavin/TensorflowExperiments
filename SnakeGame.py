class SnakeGame:
    # width: width of the snake map
    # height: height of the map
    # vWidth, vHeight: optional if the user wants the vision to be focused 
    # on the head of the snake 
    def __init__(self, width=10, height=10, vWidth=5, vHeight=5):
        self.WIDTH = width
        self.HEIGHT = height
        self.VWIDTH = vWidth
        self.VHEIGHT = vHeight
        self.STARTPOSX = int(width/2)
        self.STARTPOSY = int(height/2)

        self.mapArray=list(self.WIDTH*self.HEIGHT)
        for i in range(len(mapArray)):
            mapArray[i]=' '
    
    def printBoard():
        