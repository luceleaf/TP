import math
import random
from MapDrawings import *
from cmu_graphics import *
from LegalFunctions import *
from PIL import Image

class arrowProjectiles:
    def __init__(self, startCoords, direction):
        self.startCoords = startCoords
        self.direction = direction
        self.time = 0
        self.radius = 25
        self.image = CMUImage(Image.open('images/arrow.png'))
    
    def getStartCoords(self):
        return self.startCoords
    
    def getDirection(self):
        return self.direction
    
    def move(self, num):
        x, y = self.startCoords
        x += num
        self.startCoords = (x, y)
    
class bombProjectiles:
    def __init__(self, startCoords):
        self.startCoords = startCoords
        self.isAtEnd = False
        self.endTimer = 60
        self.radius = 15
        self.moves = []
        self.image1 = CMUImage(Image.open('images/ziggs1.png'))
        self.image2 = CMUImage(Image.open('images/ziggs2.png'))
        self.image3 = CMUImage(Image.open('images/ziggs3.png'))

    def getStartCoords(self):
        return self.startCoords
    
    def move(self, num):
        x, y = self.startCoords
        x += num
        self.startCoords = (x, y)

class karthusProjectiles:
    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.radius = 20
        self.image = CMUImage(Image.open('images/karthus.png'))

    def move(self, num):
        x, y = self.coordinates
        x += num
        self.coordinates = (x, y)

def sendProjectile(app):
    index = randrange(0,3)
    if index == 0 and len(app.arrowList) < 6:
        shootArrow(app)
    elif index == 1 and len(app.karthusList) < 6:
        shootKarthus(app)
    elif index == 2 and len(app.bombList) < 6:
        shootBomb(app)

def shootKarthus(app):
    coords = findModeCoords(app)
    app.karthusList.append(karthusProjectiles(coords))

def karthusMove(app):
    aliveKarthus = []
    for karthus in app.karthusList:
        karthus.radius += 0.2
        if karthus.radius < 40:
            aliveKarthus.append(karthus)
    app.karthusList = aliveKarthus
    print(app.karthusList)

def karthusCollision(app):
    aliveKarthus = []
    for karthus in app.karthusList:
        x, y = karthus.coordinates
        if karthus.radius > 35:
            if dist(x, y, app.charX, app.charY) <= app.charSize + karthus.radius:
                app.sprite.karthusHit()
                continue
        aliveKarthus.append(karthus)
    app.karthusList = aliveKarthus

def shootBomb(app):
    startCoords = createCoords(app)
    app.bombList.append(bombProjectiles(startCoords))

def bombMove(app):
    aliveBomb = []
    for bomb in app.bombList:
        if bomb.isAtEnd == False:
            x, y = bomb.startCoords
            bomb.moves.append((x,y))
            if notMoving(bomb.moves):
                bomb.isAtEnd = True
                continue
            moveX, moveY = app.charX, app.charY
            xDirection = direction(x, moveX)
            yDirection = direction(y, moveY)
            if isLegalOneX(app, x, y, xDirection*2, yDirection*2):
                x += xDirection*2
                y += yDirection*2
            else: 
                if isLegalOneX(app, x, y, xDirection*2, 0):
                    x += xDirection*2
                if isLegalOneX(app, x, y, 0, yDirection*2):
                    y += yDirection*2
            bomb.startCoords = (x,y)
            aliveBomb.append(bomb)
        else:
            if bomb.endTimer != 0:
                bomb.endTimer -= 1
                aliveBomb.append(bomb)
    app.bombList = aliveBomb

def bombCollision(app):
    for bomb in app.bombList:
        x, y = bomb.startCoords
        if dist(x, y, app.charX, app.charY) <= app.charSize + 10:
            bomb.isAtEnd = True
        elif bomb.isAtEnd and bomb.endTimer <= 30 and dist(x, y, app.charX, app.charY) <= app.charSize + 30:
                app.sprite.bombCollision()

def shootArrow(app):
    startCoords = createCoords(app)
    direction = chooseDirection(app)
    startX, startY = startCoords
    for wall in app.walls:
        if wall.collide(app, startX, startY):
            startCoords = createCoords(app)
    while sameSideChecker(startCoords, direction):
        direction = chooseDirection(app)
    app.arrowList.append(arrowProjectiles(startCoords, direction))

def arrowMove(app):
    aliveArrows = []
    for arrow in app.arrowList:
        x, y = arrow.startCoords
        xDirection, yDirection = arrow.direction
        if isLegalOneX(app, x, y, xDirection, yDirection):
            x += xDirection
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
        if dist(xArrow, yArrow, app.charX, app.charY) <= app.charSize + arrow.radius:
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
    karthusCoords = set()
    for karthus in app.karthusList:
        karthusCoords.add(karthus.coordinates)
    bestCoords = None
    bestCount = 0
    for coords in setCoords:
        currCount = app.charCoords.count(coords)
        if coords in karthusCoords:
            continue
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