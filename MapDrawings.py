from cmu_graphics import *
from Projectile import *

def drawStartScreen(app):
    drawRect(app.mapWidth/4 + app.mapAdd, app.mapHeight/2, app.mapWidth/2, app.mapHeight/8, 
            fill = None, border = 'Black')
    drawRect(app.mapWidth/4 + app.mapAdd, 11*app.mapHeight/16, app.mapWidth/2, app.mapHeight/8,
                fill = None, border = 'Black')
    
    drawLabel('Start', app.mapWidth/2 + app.mapAdd, app.mapHeight/2 + app.mapHeight/16,
                size = 24, bold = True)
    drawLabel('Scoreboard', app.mapWidth/2 + app.mapAdd, 12*app.mapHeight/16,
                size = 24, bold = True)
    drawLabel('Mechanics', app.mapWidth/2 + app.mapAdd, app.mapHeight/4,
                size = 60, bold = True)
    drawLabel('Practice Tool', app.mapWidth/2 + app.mapAdd, 5*app.mapHeight/16,
                size = 32, bold = True)

def drawCharacterSelect(app):
    drawLabel('Character Selection', app.mapWidth/2 + app.mapAdd, app.mapHeight/4,
                size = 60, bold = True)
    drawCircle(app.mapWidth/4 + app.mapAdd, 
               app.mapHeight/2, 40, fill = 'yellow')
    drawCircle(2*app.mapWidth/4 + app.mapAdd, 
               app.mapHeight/2, 50, fill = 'pink')
    drawCircle(3*app.mapWidth/4 + app.mapAdd, 
               app.mapHeight/2, 60, fill = 'purple')

    drawLabel('Teemo', app.mapWidth/4 + app.mapAdd, 3*app.mapHeight/4,
                size = 20, bold = True)
    drawLabel('Ahri', 2*app.mapWidth/4 + app.mapAdd, 3*app.mapHeight/4,
                size = 20, bold = True)
    drawLabel('Malphite', 3*app.mapWidth/4 + app.mapAdd, 3*app.mapHeight/4,
                size = 20, bold = True)
    
    drawLabel('the swift scout', app.mapWidth/4 + app.mapAdd, 25*app.mapHeight/32, bold = True)
    drawLabel('the nine tailed fox', 2*app.mapWidth/4 + app.mapAdd, 25*app.mapHeight/32, bold = True)
    drawLabel('shard of the monolith', 3*app.mapWidth/4 + app.mapAdd, 25*app.mapHeight/32, bold = True)

    drawLabel('Teemo is a cute yordle!', app.mapWidth/4 + app.mapAdd, 54*app.mapHeight/64, bold = True)
    drawLabel('What he lacks in health', app.mapWidth/4 + app.mapAdd, 55*app.mapHeight/64, bold = True)
    drawLabel('he makes up for with', app.mapWidth/4 + app.mapAdd, 56*app.mapHeight/64, bold = True)
    drawLabel('his speed and size.', app.mapWidth/4 + app.mapAdd, 57*app.mapHeight/64, bold = True)

    drawLabel('Ahri is a pretty vastayan!', 2*app.mapWidth/4 + app.mapAdd, 54*app.mapHeight/64, bold = True)
    drawLabel('She does not excel at', 2*app.mapWidth/4 + app.mapAdd, 55*app.mapHeight/64, bold = True)
    drawLabel('any stat but has ok', 2*app.mapWidth/4 + app.mapAdd, 56*app.mapHeight/64, bold = True)
    drawLabel('health, size, and speed.', 2*app.mapWidth/4 + app.mapAdd, 57*app.mapHeight/64, bold = True)
    
    drawLabel('Malphite is a living rock!', 3*app.mapWidth/4 + app.mapAdd, 54*app.mapHeight/64, bold = True)
    drawLabel('He is pretty slow and', 3*app.mapWidth/4 + app.mapAdd, 55*app.mapHeight/64, bold = True)
    drawLabel('large but being a rock,', 3*app.mapWidth/4 + app.mapAdd, 56*app.mapHeight/64, bold = True)
    drawLabel('he has very high health.', 3*app.mapWidth/4 + app.mapAdd, 57*app.mapHeight/64, bold = True)      

def drawMapOne(app, setWidth, setHeight, addX, addY):
    #grass portions of map
    drawRect(3*setWidth/8 + addX + app.mapAdd, addY,
             setWidth/4, setHeight, fill = 'lightGreen')
    drawRect(addX + app.mapAdd, addY,
             3*setWidth/8, 2*setHeight/8, fill = 'lightGreen')
    drawRect(5*setWidth/8 + addX + app.mapAdd, addY,
             3*setWidth/8, 2*setHeight/8, fill = 'lightGreen')
    drawRect(addX + app.mapAdd, 6*setHeight/8 + addY,
             3*setWidth/8, 2*setHeight/8, fill = 'lightGreen')
    drawRect(5*setWidth/8 + addX + app.mapAdd, 6*setHeight/8 + addY,
             3*setWidth/8, 2*setHeight/8, fill = 'lightGreen')
    #top left obstacle
    drawRect(addX + app.mapAdd, 2*setHeight/8 + addY,
             3*setWidth/8, setHeight/8, fill = 'Gray')
    #bottom left obstacle
    drawRect(addX + app.mapAdd, 5*setHeight/8 + addY,
             3*setWidth/8, setHeight/8, fill = 'Gray')
    #top right obstacle
    drawRect(5*setWidth/8 + addX + app.mapAdd, 2*setHeight/8 + addY,
             3*setWidth/8, setHeight/8, fill = 'Gray')
    #bottom right obstacle
    drawRect(5*setWidth/8 + addX + app.mapAdd, 5*setHeight/8 + addY,
             3*setWidth/8, setHeight/8, fill = 'Gray')
    #water portion of map
    drawRect(addX + app.mapAdd, 3*setHeight/8 + addY,
             2*setWidth/8, 2*setHeight/8, fill = 'lightBlue')
    drawRect(6*setWidth/8 + addX + app.mapAdd, 3*setHeight/8 + addY,
             2*setWidth/8, 2*setHeight/8, fill = 'lightBlue')
    #green portion of map
    drawRect(2*setWidth/8 + app.mapAdd + addX, 3*setHeight/8 + addY,
             setWidth/8, 2*setHeight/8, fill = 'Green')
    drawRect(5*setWidth/8 + app.mapAdd + addX, 3*setHeight/8 + addY,
             setWidth/8, 2*setHeight/8, fill = 'Green')
    #draw health tracker
    if addX == 0 and addY == 0 and app.sprite.getCurrentHealth() > 0:
        currHealthRatio = app.sprite.getCurrentHealth()/app.sprite.getTotalHealth()
        drawRect(6*setWidth/8 + app.mapAdd, 0, 
                2*setWidth/8, setHeight/8, fill = 'White', border = 'Black')
        drawRect(6*setWidth/8 + app.mapAdd, 0,
                 2*setWidth/8, setHeight/16, border = 'Black', fill = 'Gray')
        drawRect(6*setWidth/8 + app.mapAdd, 0,
                 2*setWidth/8*currHealthRatio, setHeight/16, border = 'Black', fill = 'darkRed')
        drawLabel(f'{app.sprite.getCurrentHealth()} / {app.sprite.getTotalHealth()}',
                  7*setWidth/8 + app.mapAdd, 3*setHeight/32)
        drawArrow(app)
        drawBeam(app)
        drawFish(app)s

def drawMapTwo(app, setWidth, setHeight, addX, addY):
    drawPolygon(6*setWidth/16 + addX + app.mapAdd, 6*setHeight/16 + addY,
                10*setWidth/16 + addX + app.mapAdd, 6*setHeight/16 + addY,
                10*setWidth/16 + addX + app.mapAdd, 7*setHeight/16 + addY,
                8*setWidth/16 + addX + app.mapAdd, 7*setHeight/16 + addY,
                8*setWidth/16 + addX + app.mapAdd, 9*setHeight/16 + addY,
                10*setWidth/16 + addX + app.mapAdd, 9*setHeight/16 + addY,
                10*setWidth/16 + addX + app.mapAdd, 10*setHeight/16 + addY,
                6*setWidth/16 + addX + app.mapAdd, 10*setHeight/16 + addY,
                fill = 'Gray')
    drawRect(addX + app.mapAdd, addY, 6*setWidth/16, setHeight, fill = 'Sienna')
    drawPolygon(6*setWidth/16 + addX + app.mapAdd, addY,
                setWidth + addX + app.mapAdd, addY,
                setWidth + addX + app.mapAdd, setHeight + addY,
                6*setWidth/16 + addX + app.mapAdd, setHeight + addY,
                6*setWidth/16 + addX + app.mapAdd, 10*setHeight/16 + addY,
                10*setWidth/16 + addX + app.mapAdd, 10*setHeight/16 + addY,
                10*setWidth/16 + addX + app.mapAdd, 9*setHeight/16 + addY,
                8*setWidth/16 + addX + app.mapAdd, 9*setHeight/16 + addY,
                8*setWidth/16 + addX + app.mapAdd, 7*setHeight/16 + addY,
                10*setWidth/16 + addX + app.mapAdd, 7*setHeight/16 + addY,
                10*setWidth/16 + addX + app.mapAdd, 6*setHeight/16 + addY,
                6*setWidth/16 + addX + app.mapAdd, 6*setHeight/16 + addY,
                fill = 'darkGreen')
    pass

def drawMapSelect(app):
    drawLabel('Map Selection', app.mapWidth/2 + app.mapAdd, app.mapHeight/4,
                size = 60, bold = True)
    drawMapOne(app, app.mapWidth/4, app.mapHeight/4, app.mapWidth/8, 3*app.mapHeight/8)
    drawMapTwo(app, app.mapWidth/4, app.mapHeight/4, 5*app.mapWidth/8, 3*app.mapHeight/8)
    drawRect(app.mapWidth/4 + app.mapAdd, app.mapHeight/2, app.mapWidth/4, app.mapHeight/4,
             align = 'center', fill = None, border = 'Black')
    drawRect(3*app.mapWidth/4 + app.mapAdd, app.mapHeight/2, app.mapWidth/4, app.mapHeight/4,
             align = 'center', fill = None, border = 'Black')
    drawLabel('Mid Lane', app.mapWidth/4 + app.mapAdd, 3*app.mapHeight/4,
                size = 20, bold = True)
    drawLabel('Bot Lane', 3*app.mapWidth/4 + app.mapAdd, 3*app.mapHeight/4,
                size = 20, bold = True)
    
def drawGameOver(app):
    drawRect(app.mapWidth/4 + app.mapAdd, app.mapHeight/2, app.mapWidth/2, app.mapHeight/8, 
            fill = None, border = 'Black')
    drawRect(app.mapWidth/4 + app.mapAdd, 11*app.mapHeight/16, app.mapWidth/2, app.mapHeight/8,
                fill = None, border = 'Black')
    
    drawLabel('Try Again', app.mapWidth/2 + app.mapAdd, app.mapHeight/2 + app.mapHeight/16,
                size = 24, bold = True,)
    drawLabel('Main Menu', app.mapWidth/2 + app.mapAdd, 12*app.mapHeight/16,
                size = 24, bold = True)
    drawLabel('Game Over', app.mapWidth/2 + app.mapAdd, app.mapHeight/4,
                size = 60, bold = True, fill = 'Red')
    drawLabel(f'You survived {int(app.counter/30)} seconds', app.mapWidth/2 + app.mapAdd,
              6*app.mapHeight/16, size = 24)
    
# open function, online
def drawScoreboard(app):
    drawLabel('Scoreboard', app.mapWidth/2 + app.mapAdd, app.mapHeight/4,
                size = 60, bold = True)
    index = 0
    for line in app.scores:
        if line == 0:
            drawLabel('None', app.mapWidth/2 +app.mapAdd, (6+index)*app.mapHeight/16, size = 24)
        else:
            drawLabel(line, app.mapWidth/2 + app.mapAdd, (6+index)*app.mapHeight/16, size = 24)
        index += 1

def drawArrow(app):
    for arrow in app.arrowList:
        x, y = arrow[0]
        drawCircle(x, y, 20, fill = 'Black')

def drawBeam(app):
    for beam in app.beamList:
        xStart, yStart = beam.startCoords
        xEnd, yEnd = beam.endCoords
        xMidpoint = abs(xStart - xEnd)
        yMidpoint = abs(yStart - yEnd)
        if beam.time > 60:
            drawRect(xMidpoint, yMidpoint, 2*app.mapWidth, 10, 
                     align = 'center', rotateAngle = beam.angle, fill = 'Yellow')
        elif beam.time > 30:
            drawRect(xMidpoint, yMidpoint, 2*app.mapWidth, 20, 
                     align = 'center', rotateAngle = beam.angle, fill = 'Yellow')
        else:
            drawRect(xMidpoint, yMidpoint, 2*app.mapWidth, 30, 
                     align = 'center', rotateAngle = beam.angle, fill = 'Yellow')
            
def drawFish(app):
    for fish in app.fishList:
        if fish.isAtEnd == False:
            x, y = fish.startCoords
            drawCircle(x, y, 10, fill = 'lightBlue')
        else:
            if fish.endTimer == 0:
                color = 'Black'
            else:
                color = 'Blue'
            x, y = fish.endCoords
            drawCircle(x, y, 30, fill = color)

        



