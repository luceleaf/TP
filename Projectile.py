import math
import random
from MapDrawings import *
from cmu_graphics import *
from LegalFunctions import *

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
    
class fishProjectiles:
    def __init__(self, startCoords):
        self.startCoords = startCoords
        self.isAtEnd = False
        self.endTimer = 60
        self.moves = []

    def getStartCoords(self):
        return self.startCoords
    
class bombProjectiles:
    def __init__(self, startCoords, endCoords):
        self.startCoords = startCoords
        self.endCoords = endCoords
        self.endTimer = 60
        self.isAtEnd = False
        self.countStationary = 0
        self.moves = []

    def getStartCoords(self):
        return self.startCoords
    
    def getEndCoords(self):
        return self.endCoords

def sendProjectile(app):
    index = randrange(0,3)
    if index == 0:
        shootArrow(app)
    elif index == 1:
        shootBomb(app)
    elif index == 2:
        shootFish(app)

def shootBomb(app):
    startCoords = createCoords(app)
    while spawninWall(app, startCoords):
        startCoords = createCoords(app)
    endCoords = findModeCoords(app)
    app.bombList.append(bombProjectiles(startCoords, endCoords))

def bombMove(app):
    aliveBombs = []
    for bomb in app.bombList:
        x, y = bomb.startCoords
        bomb.moves.append((x,y))
        xEnd, yEnd = bomb.endCoords
        if x == xEnd and y == yEnd or notMoving(bomb.moves):
            bomb.isAtEnd = True
        moveX, moveY = bomb.endCoords
        xDirection = direction(x, moveX)
        yDirection = direction(y, moveY)
        if isLegalOneX(app, x, xDirection, y):
            x += xDirection
        if isLegalOneY(app, y, yDirection, x):
            y += yDirection
        if bomb.isAtEnd == False:
            bomb.startCoords = (x,y)
            aliveBombs.append(bomb)
        else:
            if bomb.endTimer != 0:
                bomb.endTimer -= 1
                aliveBombs.append(bomb)
    app.bombList = aliveBombs

def bombCollision(app):
    aliveBombs = []
    for bomb in app.bombList:
        x, y = bomb.startCoords
        if not bomb.isAtEnd and dist(x, y, app.charX, app.charY) <= app.charSize + 10:
            app.sprite.smallBombCollision()
        elif bomb.isAtEnd and dist(x, y, app.charX, app.charY) <= app.charSize + 30:
            app.sprite.largeBombCollision()
        else:
            aliveBombs.append(bomb)
    app.bombList = aliveBombs

def shootFish(app):
    startCoords = createCoords(app)
    app.fishList.append(fishProjectiles(startCoords))

def fishMove(app):
    aliveFish = []
    for fish in app.fishList:
        if fish.isAtEnd == False:
            x, y = fish.startCoords
            fish.moves.append((x,y))
            if notMoving(fish.moves):
                fish.isAtEnd = True
                continue
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
        elif fish.isAtEnd and fish.endTimer <= 30 and dist(x, y, app.charX, app.charY) <= app.charSize + 30:
                app.sprite.fishCollision()

def shootArrow(app):
    startCoords = createCoords(app)
    direction = chooseDirection(app)
    while spawninWall(app, startCoords):
        startCoords = createCoords(app)
    while sameSideChecker(startCoords, direction):
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

def dist(x0, y0, x1, y1):
    return ((x1-x0)**2 + (y1-y0)**2)**(1/2)

def direction(original, new):
    if original > new:
        return -1
    return 1

def findModeCoords(app):
    setCoords = set(app.charCoords)
    bestCoords = None
    bestCount = 0
    for coords in setCoords:
        currCount = app.charCoords.count(coords)
        if currCount > bestCount:
            bestCount = currCount
            bestCoords = coords
    return bestCoords
    
def notMoving(moves):
    count = 0
    if len(moves) > 2:
        return False
    for i in range (1, len(moves)):
        if moves[i] == moves[i-2]:
            count +=1
    return count > 5