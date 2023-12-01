from cmu_graphics import *

class Wall:
    def __init__(self, topLeftX, topLeftY, setWidth, setHeight, align,color):
        self.topLeftX = topLeftX
        self.topLeftY = topLeftY
        self.setWidth = setWidth
        self.setHeight = setHeight
        self.wallAlign = align
        self.color = color

    def draw(self, app):
        drawRect(self.topLeftX + app.mapAdd, self.topLeftY, self.setWidth*2, self.setHeight,
                 fill = self.color, align = self.wallAlign)
        
    def move(self, num):
        self.topLeftX+=num

    def collide(self, app, posX, posY):
        cX = posX
        cY = posY
        rightXBound = 0
        leftXBound = 0
        topYBound = 0
        botYBound = 0
        if (self.wallAlign == "right-top"):
            rightXBound = self.topLeftX
            leftXBound = self.topLeftX - self.setWidth*2
            topYBound = self.topLeftY
            botYBound = self.topLeftY + self.setHeight
        if(self.wallAlign == "left-top"):
            rightXBound = self.topLeftX+ self.setWidth*2
            leftXBound = self.topLeftX 
            topYBound = self.topLeftY
            botYBound = self.topLeftY + self.setHeight
        if (leftXBound <= cX <= rightXBound and 
        topYBound <= cY <= botYBound):
            return True
        return False

        


class GrassWater:
    def __init__(self, xStart, yStart, setWidth, setHeight, blockAlign, color):
        self.xStart = xStart
        self.yStart = yStart
        self.setWidth = setWidth
        self.setHeight = setHeight
        self.align = blockAlign
        self.color = color

    def draw(self, app):
        drawRect(self.xStart + app.mapAdd, self.yStart, self.setWidth, self.setHeight,
                 fill = self.color, align = self.align)
        
    def move(self, num):
        self.xStart += num

        