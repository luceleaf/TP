from cmu_graphics import *
from Character import *
from MapDrawings import *
from LegalFunctions import *
from Projectile import *
from wall import *
from PIL import Image
import random
from Upgrades import *

def onAppStart(app):
    fullGameReset(app)

def fullGameReset(app):
    app.startScreen = True
    app.scoreboard = False
    app.characterSelect = False
    app.ruleScreen = False
    app.map1 = False
    app.gamePaused = False
    app.gameOver = False
    app.width = 700
    app.height = 700
    app.mapWidth, app.mapHeight = app.width, app.height
    app.mapAdd = 0
    app.square = True
    app.charX = app.mapWidth/2
    app.charY = app.mapHeight/2
    app.moveToX = None
    app.moveToY = None
    app.sprite = None
    app.background = 'White'
    app.scores = []
    app.counter = 0
    app.amountMoved = 0
    app.edgeX = app.mapWidth/8
    app.projectiles = ['arrow', 'beam', 'fish']
    app.arrowList = []
    app.charCoords = []
    app.fishList = []
    app.karthusList = []
    app.upgradesList = []
    app.activeUpgrade = None
    wall1 = Wall(app.mapAdd+3*app.mapWidth/8, 2*app.mapHeight/8,
             6*app.mapWidth/8, app.mapHeight/8, 'right-top', "grey")
    wall2 = Wall(app.mapAdd + 5*app.mapHeight/8, 2*app.mapHeight/8,
             6*app.mapWidth/8, app.mapHeight/8, 'left-top', "grey")
    wall3 = Wall(3*app.mapWidth/8 + app.mapAdd, 5*app.mapHeight/8,
             6*app.mapWidth/8, app.mapHeight/8,'right-top', "grey")
    wall4 = Wall(5*app.mapWidth/8 + app.mapAdd, 5*app.mapHeight/8,
             6*app.mapWidth/8, app.mapHeight/8, 'left-top', "grey")
    app.walls = [wall1,wall2,wall3,wall4]
    riverLeft = GrassWater(3*app.mapWidth/8 + app.mapAdd, 3*app.mapHeight/8, app.mapWidth/8, 2*app.mapHeight/8, 'right-top', 'Green')
    grassLeft = GrassWater(2*app.mapWidth/8 + app.mapAdd, 3*app.mapHeight/8, 8*app.mapWidth/8, 2*app.mapHeight/8, 'right-top', 'lightBlue')
    riverRight = GrassWater(6*app.mapWidth/8 + app.mapAdd, 3*app.mapHeight/8, 8*app.mapWidth/8, 2*app.mapHeight/8, 'left-top', 'lightBlue')
    grassRight = GrassWater(5*app.mapWidth/8 + app.mapAdd, 3*app.mapHeight/8, app.mapWidth/8, 2*app.mapHeight/8, 'left-top', 'Green')
    app.objects = [riverLeft, riverRight, grassLeft, grassRight]
    app.charSize = None
    scores = open('scoreboard.txt', 'r')
    for line in scores:
        app.scores.append(int(float(line)))

def softReset(app):
    app.counter = 0
    app.arrowList = []
    app.charCoords = []
    app.fishList = []
    app.karthusList = []
    app.hasUpgrade = False
    app.gamePaused = False

def onStep(app):
    if app.width != app.height:
        canvasSize(app)
        app.square = False
    if app.map1 and not app.gamePaused:
        healthChecker(app)
        app.counter +=1
        if app.sprite.stunTime != 0:
            characterMove(app, app.sprite.speed)
        else:
            app.sprite.lowerStun(app)
        arrowMove(app)
        arrowCollision(app)
        fishMove(app)
        fishCollision(app)
        karthusMove(app)
        karthusCollision(app)
        upgradeCollision(app)
        upgradeChecker(app)
    if app.counter != 0 and app.counter % 60 == 0:
        addCoordinates(app)
        sendProjectile(app)
    if app.counter != 0 and app.counter % 300 == 0:
        sendUpgrade(app)

def addCoordinates(app):
    if len(app.charCoords) > 50:
        app.charCoords.pop(0)
    app.charCoords.append((app.charX, app.charY))

def characterMove(app, stepNum):
    moveX = 0
    moveY = 0
    if app.moveToX != None and app.moveToX != app.charX:
        if app.charX > app.moveToX:
            moveX = -1*stepNum
        else:
            moveX = 1*stepNum
    if app.moveToY != None and app.moveToY != app.charX:
        if app.charY > app.moveToY:
            moveY = -1*stepNum
        elif app.charY < app.moveToY:
            moveY = 1*stepNum
        
    if isLegalOneX(app, app.charX, app.charY, moveX, moveY):
        app.charX += moveX
        app.charY += moveY
        app.amountMoved += moveX
        if moveX > 0 and app.charX > app.mapWidth - app.edgeX:
            screenMoveLeft(app, stepNum)
        elif moveX < 0 and app.charX < app.edgeX:
                screenMoveRight(app, stepNum)
        
def screenMoveLeft(app, stepNum):
    if(app.amountMoved < app.mapWidth):
        app.charX = app.mapWidth - app.edgeX
        for wallX in app.walls:
            wallX.move(-1*stepNum)
        for object in app.objects:
            object.move(-1*stepNum)
        for arrow in app.arrowList:
            arrow.move(-1*stepNum)
        for karthus in app.karthusList:
            karthus.move(-1*stepNum)
        for fish  in app.fishList:
            fish.move(-1*stepNum)
        for upgrade in app.upgradesList:
            upgrade.move(stepNum)

def screenMoveRight(app, stepNum):
    if(app.amountMoved > -app.mapWidth):
        app.charX = app.edgeX
        for wallX in app.walls:
            wallX.move(stepNum)
        for object in app.objects:
            object.move(stepNum)
        for arrow in app.arrowList:
            arrow.move(stepNum)
        for karthus in app.karthusList:
            karthus.move(stepNum)
        for fish  in app.fishList:
            fish.move(stepNum)
        for upgrade in app.upgradesList:
            upgrade.move(stepNum)
        
def canvasSize(app):
    mapSize = min(app.width, app.height)
    app.mapWidth = app.mapHeight = mapSize
    if max(app.width, app.height) == app.width:
        app.mapAdd = (max(app.width, app.height) - mapSize)/2

def redrawAll(app):
    if app.startScreen:
        drawStartScreen(app)
    elif app.scoreboard:
        drawScoreboard(app)
    elif app.characterSelect:
        drawCharacterSelect(app)
    elif app.ruleScreen:
        drawRuleScreen(app)
    elif app.map1:
        drawMapOne(app, app.mapWidth, app.mapHeight, 0, 0)
        drawCharacter(app)
    elif app.gameOver:
        drawGameOver(app)
    if app.gamePaused:
        drawPauseScreen(app)

def onMousePress(app, mouseX, mouseY):
    if app.map1 == True:
        app.moveToX = mouseX
        app.moveToY = mouseY
    elif app.startScreen == True:
        if (app.mapWidth/4 + app.mapAdd <= mouseX <= app.mapWidth/4 + app.mapWidth/2 + app.mapAdd and
            app.mapHeight/2 <= mouseY <= app.mapHeight/2 + app.mapHeight/8):
            app.startScreen = False
            app.characterSelect = True
        elif (app.mapWidth/4 + app.mapAdd <= mouseX <= app.mapWidth/4 + app.mapWidth/2 + app.mapAdd and
              11*app.mapHeight/16 <= mouseY <= 11*app.mapHeight/16 + app.mapHeight/8):
            app.startScreen = False
            app.scoreboard = True
    elif app.characterSelect == True:
        if dist(mouseX, mouseY, app.mapWidth/4 + app.mapAdd, app.mapHeight/2) <= 40:
            app.characterSelect = False
            app.ruleScreen = True
            app.sprite = teemo
            app.charSize = app.sprite.radius
            app.background = 'lightGreen'
        elif dist(mouseX, mouseY, 2*app.mapWidth/4 + app.mapAdd, app.mapHeight/2) <= 50:
            app.characterSelect = False
            app.ruleScreen = True
            app.sprite = ahri
            app.charSize = app.sprite.radius
            app.background = 'lightGreen'
        elif dist(mouseX, mouseY, 3*app.mapWidth/4 + app.mapAdd, app.mapHeight/2) <= 60:
            app.characterSelect = False
            app.ruleScreen = True
            app.sprite = malphite
            app.charSize = app.sprite.radius
            app.background = 'lightGreen'
    elif app.gameOver == True:
        if (app.mapWidth/4 + app.mapAdd <= mouseX <= app.mapWidth/4 + app.mapWidth/2 + app.mapAdd and
            app.mapHeight/2 <= mouseY <= app.mapHeight/2 + app.mapHeight/8):
            app.sprite.resetCurrentHealth()
            softReset(app)
            app.map1 = True   
            app.gameOver = False
        elif (app.mapWidth/4 + app.mapAdd <= mouseX <= app.mapWidth/4 + app.mapWidth/2 + app.mapAdd and
            11*app.mapHeight/16 <= mouseY <= 11*app.mapHeight/16 + app.mapHeight/8):
            app.gameOver = False
            app.startScreen = True
            fullGameReset(app)

def onKeyPress(app, key):
    if key == 'left':
        if app.map1 == True:
            app.map1 = False
            app.mapSelect = True
        elif app.ruleScreen == True:
            app.ruleScreen = False
            app.characterSelect = True
        elif app.characterSelect == True:
            app.characterSelect = False
            app.startScreen = True
        elif app.scoreboard == True:
            app.scoreboard = False
            app.startScreen = True
    if app.ruleScreen:
        if key == 'space':
            app.ruleScreen = False
            app.map1 = True
    if app.map1:
        if key == 'f' and app.activeUpgrade != None:
            upgradeUse(app)
        if key == 'p':
            app.gamePaused = not app.gamePaused

def dist(x0, y0, x1, y1):
    return ((x1-x0)**2 + (y1-y0)**2)**(1/2)

#used internet for clearing scoreboard method
def updateScoreboard(app):
    currTime = app.counter/30
    app.scores.append(currTime)
    app.scores.sort(reverse = True)
    app.scores.pop()
    open('scoreboard.txt', 'w').close()
    with open('scoreboard.txt', 'w') as f:
        for score in app.scores:
            f.write(str(int(score)))

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
    
def direction(original, new):
    if original > new:
        return -1
    return 1

def healthChecker(app):
    if app.sprite.getCurrentHealth() <= 0:
        app.gameOver = True
        app.background = 'White'
        app.map1 = False
        updateScoreboard(app)

def upgradeUse(app):
    if app.activeUpgrade == 'shield':
        missingHP = app.sprite.totalHealth - app.sprite.currHealth
        app.sprite.createShield(missingHP*0.75)
    elif app.activeUpgrade == 'flash':
        characterMove(app, 50)
    else:
        app.sprite.heal()
    app.activeUpgrade = None

def upgradeChecker(app):
    if app.sprite.timer != 0:
        app.sprite.timer -= 1
        if app.sprite.timer == 0:
            app.sprite.shield = 0
            app.sprite.speed = app.sprite.baseSpeed

runApp()