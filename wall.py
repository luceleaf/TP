from cmu_graphics import *

class Wall:
    def __init__(self, topLeftX, topLeftY, setWidth, setHeight):
        self.topLeftX = topLeftX
        self.topLeftY = topLeftY
        self.setWidth = setWidth
        self.setHeight = setHeight

    def draw(self, app):
        drawRect(self.topLeftX + app.mapAdd, self.topLeftY, self.setWidth, self.setHeight,
                 fill = 'Gray')