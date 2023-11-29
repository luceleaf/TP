import time
import math
from MapDrawings import *
from cmu_graphics import *
from LegalFunctions import *

def createCoords(app):
    choice = randrange(1,5)
    if choice == 1:
        return (app.mapAdd, randrange(0, app.mapHeight))
    elif choice == 2:
        return (app.mapWidth + app.mapAdd, randrange(0, app.mapHeight))
    elif choice == 3:
        return (randrange(app.mapAdd, app.mapWidth+app.mapAdd), 0)
    elif choice == 4:
        return (randrange(app.mapAdd, app.mapWidth+app.mapAdd), app.mapHeight)
    
def chooseDirection(app):
    directions = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
    choice = randrange(0, 4)
    return directions[choice]

def sendProjectile(app):
    index = randrange(0,3)
    if index == 0:
        shootArrow(app)
    elif index == 1:
        shootBeam(app)
    elif index == 2:
        shootFish(app)

def shootBeam(app):
    startCoords = createCoords(app)
    playerLocation = (app.charX, app.charY)
    app.beamList.append(beamProjectiles(startCoords, playerLocation, app.mapWidth, app.mapHeight))

def shootFish(app):
    startCoords = createCoords(app)
    app.fishList.append(fishProjectiles(startCoords))

def fishMove(app):
    aliveFish = []
    for fish in app.fishList:
        if fish.isAtEnd == False:
            x, y = fish.startCoords
            moveX, moveY = app.charX, app.charY
            xDirection = direction(x, moveX)
            yDirection = direction(y, moveY)
            if isLegalOneX(app, x, xDirection, y):
                x += xDirection*2
            if isLegalOneY(app, y, yDirection, x):
                y += yDirection*2
            fish.startCoords = (x,y)
            aliveFish.append(fish)
        else:
            if fish.endTimer != 0:
                fish.endTimer -= 1
                aliveFish.append(fish)
    app.fishList = aliveFish

def fishCollision(app):
    for fish in app.fishList:
        x, y = fish.startCoords
        if dist(x, y, app.charX, app.charY) <= app.charSize + 10:
            fish.isAtEnd = True
            if fish.endTimer <= 30:
                app.sprite.fishCollision()

def shootArrow(app):
    startCoords = createCoords(app)
    direction = chooseDirection(app)
    while sameSideChecker(startCoords, direction):
        startCoords = createCoords(app)
        direction = chooseDirection(app)
    app.arrowList.append(arrowProjectiles(startCoords, direction))

def arrowMove(app):
    aliveArrows = []
    for arrow in app.arrowList:
        x, y = arrow.startCoords
        xDirection, yDirection = arrow.direction
        if isLegalOneX(app, x, xDirection, y):
            x += xDirection
        else: 
            xDirection *= -1
        if isLegalOneY(app, y, yDirection, x):
            y += yDirection
        else:
            yDirection *= -1
        arrow.startCoords = (x, y)
        arrow.direction = (xDirection, yDirection)
        if not (x == 0 or x == app.mapWidth or y == 0 or y == app.mapHeight):
            arrow.time += 1
            aliveArrows.append(arrow)
    app.arrowList = aliveArrows

def arrowCollision(app):
    aliveArrows = []
    for arrow in app.arrowList:
        xArrow, yArrow = arrow.startCoords
        if dist(xArrow, yArrow, app.charX, app.charY) <= app.charSize + arrow.arrowSize:
            app.sprite.arrowHit(arrow.time)
        else:
            aliveArrows.append(arrow)
    app.arrowList = aliveArrows

def sameSideChecker(startCoords, direction):
    x, y = startCoords
    xDirection, yDirection = direction
    if x == 0 and xDirection == -1:
        return True
    elif x == app.mapWidth and xDirection == 1:
        return True
    elif y == 0 and yDirection == -1:
        return True
    elif y == app.mapHeight and yDirection == 1:
        return True
    return False

def dist(x0, y0, x1, y1):
    return ((x1-x0)**2 + (y1-y0)**2)**(1/2)

def direction(original, new):
    if original > new:
        return -1
    return 1

class arrowProjectiles:
    def __init__(self, startCoords, direction):
        self.startCoords = startCoords
        self.direction = direction
        self.time = 0
        self.arrowSize = 20
    
    def getStartCoords(self):
        return self.startCoords
    
    def getDirection(self):
        return self.direction
    
    def __repr__(self):
        return (f'''name = {self.name},
                size = {self.size}''')
    

class beamProjectiles:
    def __init__(self, startCoords, playerLocation, mapWidth, mapHeight):
        self.startCoords = startCoords
        self.playerLocation = playerLocation
        x0, y0 = self.startCoords
        x1, y1 = self.playerLocation
        self.slopeY = y1-y0
        self.slopeX = x1-x0
        self.time = 90
        self.mapWidth = mapWidth
        self.mapHeight = mapHeight
        #finds end coords
        x0, y0 = self.startCoords
        xEnd = x0 + self.slopeX
        yEnd = y0 + self.slopeY
        while (0 < xEnd < self.mapWidth or
               0 < yEnd < self.mapHeight):
            xEnd += self.slopeX
            yEnd += self.slopeY
        if xEnd < 0:
            xEnd = 0
            yEnd = y0 + (y1-y0)/(x1-x0)*xEnd
        elif xEnd > self.mapWidth:
            xEnd = self.mapWidth
            yEnd = y0 + (y1-y0)/(x1-x0)*xEnd
        elif yEnd < 0:
            yEnd = 0
            xEnd = y0 + (y1-y0)/(x1-x0)*yEnd
        elif yEnd > self.mapHeight:
            yEnd = self.mapHeight
            xEnd = y0 + (y1-y0)/(x1-x0)*yEnd
        self.endCoords = xEnd, yEnd
        #finds angle
        x0, y0 = self.startCoords
        x1, y1 = self.endCoords
        thetaStart = math.atan2(y0, x0)
        thetaEnd = math.atan2(y1, x1)
        r = (thetaEnd - thetaStart) * (180/math.pi)
        if r < 0:
            r%= 360
        self.angle = r

    def getStartCoords(self):
        return self.startCoords
    
    def getPlayerLocation(self):
        return self.playerLocation
    
    def getTime(self):
        return self.time
    
    def lowerTime(self):
        self.time -= 1

class fishProjectiles:
    def __init__(self, startCoords):
        self.startCoords = startCoords
        self.isAtEnd = False
        self.endTimer = 60

    def getStartCoords(self):
        return self.startCoords
    
    def getEndCoords(self):
        return self.endCoords
    
