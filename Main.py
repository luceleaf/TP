from cmu_graphics import *
from Character import *
from MapDrawings import *

def onAppStart(app):
    app.startScreen = True
    app.scoreboard = False
    app.characterSelect = False
    app.mapSelect = False
    app.map1 = False
    app.map2 = False
    app.gameOver = False
    app.width = 700
    app.height = 700
    app.mapWidth, app.mapHeight = app.width, app.height
    app.mapAdd = 0
    app.square = True
    app.mathNumber = (4*(2)**(1/2)- 3)/(24*(2)**(1/2))
    app.charX = app.mapWidth/2
    app.charY = app.mapHeight/2
    app.moveToX = None
    app.moveToY = None
    app.sprite = None
    app.counter = 0
    app.scores = []
    scores = open('scoreboard.txt', 'r')
    for line in scores:
        app.scores.append(int(line))


def onStep(app):
    if app.width != app.height:
        canvasSize(app)
        app.square = False
    if app.moveToX != None and app.moveToX != app.charX:
        if app.charX > app.moveToX:
            app.charX -= 1
        else:
            app.charX += 1
    if app.moveToY != None and app.moveToY != app.charY:
        if app.charY > app.moveToY:
            app.charY -= 1
        else:
            app.charY += 1
    if app.map1 == True or app.map2 == True:
        app.counter +=1
    isLegal(app)
        
def canvasSize(app):
    mapSize = min(app.width, app.height)
    app.mapWidth = app.mapHeight = mapSize
    if max(app.width, app.height) == app.width:
        app.mapAdd = (max(app.width, app.height) - mapSize)/2

def redrawAll(app):
    if app.startScreen == True:
        drawStartScreen(app)
    elif app.scoreboard == True:
        drawScoreboard(app)
    elif app.characterSelect == True:
        drawCharacterSelect(app)
    elif app.mapSelect == True:
        drawMapSelect(app)
    elif app.map1 == True:
        drawMapOne(app, app.mapWidth, app.mapHeight, 0, 0)
        drawCircle(app.charX, app.charY, 5, fill = app.sprite.getColor())
    elif app.map2 == True:
        drawMapTwo(app, app.mapWidth, app.mapHeight, 0, 0)
        drawCircle(app.charX, app.charY, 5, fill = app.sprite.getColor())
    elif app.gameOver == True:
        drawGameOver(app)
    if app.square == False:
        drawRect(app.mapAdd, 0, app.mapWidth, app.mapHeight, 
                 fill = None, border = 'Black')

def onMousePress(app, mouseX, mouseY):
    if app.map1 == True or app.map2 == True:
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
            app.mapSelect = True
            app.sprite = teemo
        elif dist(mouseX, mouseY, 2*app.mapWidth/4 + app.mapAdd, app.mapHeight/2) <= 50:
            app.characterSelect = False
            app.mapSelect = True
            app.sprite = ahri
        elif dist(mouseX, mouseY, 3*app.mapWidth/4 + app.mapAdd, app.mapHeight/2) <= 60:
            app.characterSelect = False
            app.mapSelect = True
            app.sprite = malphite
    elif app.mapSelect == True:
        if (app.mapWidth/8 <= mouseX <= app.mapWidth/8 + app.mapWidth/4 and
            3*app.mapHeight/8 <= mouseY <= 3*app.mapHeight/8+app.mapHeight/4):
            app.mapSelect = False
            app.map1 = True
        elif (5*app.mapWidth/8 <= mouseX <= 5*app.mapWidth/8 + app.mapWidth/4 and
            3*app.mapHeight/8 <= mouseY <= 3*app.mapHeight/8+app.mapHeight/4):
            app.mapSelect = False
            app.map2 = True

def onKeyPress(app, key):
    if key == 'left':
        if app.map1 == True:
            app.map1 = False
            app.mapSelect = True
        elif app.map2 == True:
            app.map2 = False
            app.mapSelect = True
        elif app.mapSelect == True:
            app.mapSelect = False
            app.characterSelect = True
        elif app.characterSelect == True:
            app.characterSelect = False
            app.startScreen = True
        elif app.scoreboard == True:
            app.scoreboard = False
            app.startScreen = True

def isLegal(app):
    if (app.mathNumber*app.width < app.charX < 2*app.mathNumber*app.width) and \
    (1/3*app.mapHeight - app.mathNumber < app.charY < 1/3*app.mapHeight):
        app.charX = app.charY = 0
    pass

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
            f.write(score)

runApp()