class SnakeGame:
    import random
    from dataclasses import dataclass

    @dataclass
    class Point:
        x=int
        y=int
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
        self.snakeArray = [self.Point(self.STARTPOSX, self.STARTPOSY)]
        self.FRUITX = 0
        self.FRUITY = 0
        self.gameState = 0

        self.mapArray=list(self.WIDTH*self.HEIGHT)
        for i in range(len(self.mapArray)):
            self.mapArray[i]=' '
    
    def printBoard(self):
        for y in range(self.HEIGHT):
            for x in range(self.WIDTH):
                print(self.mapArray[y*self.WIDTH+x], end='')
            print()
    
    def clearBoard(self):
        for i in range(len(self.mapArray)):
            self.mapArray[i]=' '
    
    def spawnFruit(self):
        fruitNotPlaced = True
        fruitx=0
        fruity=0
        while fruitNotPlaced:
            fruitx = self.random.randint(0,self.WIDTH-1)
            fruity = self.random.randint(0,self.HEIGHT-1)
            fruitNotPlaced = False
            for i in self.snakeArray:
                if fruitx==i.x and fruity==i.y:
                    print("fruit spawned in snake")
                    fruitNotPlaced = True
                    # un comment this to enable the snake to get multiple fruits if lucky
                    #self.snakeArray.append(self.Point(self.snakeArray[-1].x, self.snakeArray[-1].y))
        self.FRUITX = fruitx
        self.FRUITY = fruity
        self.mapArray[self.FRUITY*self.WIDTH+self.FRUITX]='@'

    def move(self, dir):
        for i in range(len(self.snakeArray)-1):
            self.snakeArray[-i-1].x = self.snakeArray[-i-2].x
            self.snakeArray[-i-1].y = self.snakeArray[-i-2].y
            self.mapArray[self.snakeArray[-i-1].y*self.WIDTH+self.snakeArray[-i-1].x]='o'
        if dir==0:
            self.snakeArray[0].y-=1
            if self.snakeArray[0].y<0:
                self.snakeArray[0].y=self.HEIGHT-1
        elif dir==1:
            self.snakeArray[0].x=(self.snakeArray[0].x+1)%self.WIDTH
        elif dir==2:
            self.snakeArray[0].y=(self.snakeArray[0].y+1)%self.HEIGHT
        elif dir==3:
            self.snakeArray[0].x-=1
            if self.snakeArray[0].x<0:
                self.snakeArray[0].x=self.WIDTH-1
        self.mapArray[self.snakeArray[0].y*self.WIDTH+self.snakeArray[0].x]='O'
    
    def checkCollisions(self):
        gotFruit = False
        gameOver = False
        if self.snakeArray[0].x == self.FRUITX and self.snakeArray[0].y == self.FRUITY:
            self.snakeArray.append(self.Point(self.snakeArray[-1].x, self.snakeArray[-1].y))
            self.gameState=1
            gotFruit=True
        for i in self.snakeArray:
            if self.snakeArray[0].x == i.x and self.snakeArray[0].y == i.y:
                gameState=-1
                gameOver = True
        if not gotFruit and not gameOver:
            self.gameState = 0  
        
    def update(self, dir):
        if(gameState!=-1):
            self.clearBoard()
            self.mapArray[self.FRUITY*self.WIDTH+self.FRUITX]='@'
            self.move(dir)
            self.checkCollisions()
            if self.gameState == 1:
                self.spawnFruit()
        else:
            print("Game is over, not updating until new game is called")

    def newGame(self):
        self.snakeArray = [self.Point(self.STARTPOSX, self.STARTPOSY)]
        self.FRUITX = 0
        self.FRUITY = 0
        self.gameState = 0
        for i in range(len(self.mapArray)):
            self.mapArray[i]=' '

    def getGameState(self):
        return self.gameState
    def getBoard(self):
        return self.mapArray

if __name__== "__main__":
    print("This is the demo version of snake game to verify that it is working \ninput 4 to quit")
    dir = 0
    while dir!=4:
        dir = input("input dir: ")
