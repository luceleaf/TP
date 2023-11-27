from cmu_graphics import *

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
    drawRect(setWidth/2+addX+app.mapAdd, setHeight/2+addY, 
             setWidth, 1/4*setHeight, align = 'center', 
             rotateAngle = 225, fill = 'lightGreen')
    drawPolygon(addX+app.mapAdd, addY, 
                setWidth/3 + addX+app.mapAdd, addY, 
                addX+app.mapAdd, setHeight/3+addY, 
                fill = 'lightGreen')
    drawPolygon(setWidth+addX+app.mapAdd, setHeight+addY,
                setWidth*2/3+addX+app.mapAdd, setHeight+addY,
                setWidth+addX+app.mapAdd, setHeight*2/3+addY,
                fill = 'lightGreen')
    ratio = 2.5
    # top left obstacle
    drawPolygon(addX+app.mapAdd, setHeight*1/3+addY,
                setWidth*app.mathNumber + addX+app.mapAdd, setHeight*(1/3-app.mathNumber)+addY,
                ratio*setWidth*app.mathNumber + addX+app.mapAdd, setHeight*(1/3+ (ratio-2)*app.mathNumber)+addY,
                addX+app.mapAdd, setHeight*(1/3+3*app.mathNumber)+addY+app.mapAdd,
                fill = 'Gray')
    # top right obstacle
    drawPolygon(setWidth*1/3 + addX+app.mapAdd, addY,
                setWidth*(1/3-app.mathNumber) + addX+app.mapAdd, setHeight*app.mathNumber+addY,
                setWidth*(1/3+(ratio-2)*app.mathNumber) + addX+app.mapAdd, ratio*setHeight*app.mathNumber+addY,
                setWidth*(1/3+3*app.mathNumber) + addX+app.mapAdd, addY,
                fill = 'Gray')
    # bottom left obstacle
    drawPolygon(setWidth*2/3 + addX+app.mapAdd, setHeight+addY,
                setWidth*(2/3+app.mathNumber) + addX+app.mapAdd, setHeight - setHeight*app.mathNumber+addY,
                setWidth*(2/3-(ratio-2)*app.mathNumber) + addX+app.mapAdd, setHeight - ratio*setHeight*app.mathNumber+addY,
                setWidth*(2/3-3*app.mathNumber) + addX+app.mapAdd, setHeight+addY,
                fill = 'Gray')
    # bottom right obstacle
    drawPolygon(setWidth + addX+app.mapAdd, setHeight*2/3+addY,
                setWidth - setWidth*app.mathNumber + addX+app.mapAdd, setHeight*(2/3+app.mathNumber)+addY,
                setWidth -  ratio*setWidth*app.mathNumber + addX+app.mapAdd, setHeight*(2/3 - (ratio-2)*app.mathNumber)+addY,
                setWidth + addX+app.mapAdd, setHeight*(2/3-3*app.mathNumber)+addY,
                fill = 'Gray')
    
    #left dark grass patch
    drawPolygon(ratio*setWidth*app.mathNumber + addX+app.mapAdd, setHeight*(1/3+ (ratio-2)*app.mathNumber)+addY,
                app.mathNumber*setWidth + addX+app.mapAdd, setHeight*(1/3+2*app.mathNumber)+addY,
                setWidth*(2/3-2*app.mathNumber) + addX+app.mapAdd, setHeight*(1-app.mathNumber)+addY,
                setWidth*(2/3-(ratio-2)*app.mathNumber) + addX+app.mapAdd, setHeight - ratio*setHeight*app.mathNumber+addY,
                fill = 'Green')
    
    #right dark grass patch
    drawPolygon(setWidth*(1/3+(ratio-2)*app.mathNumber) + addX+app.mapAdd, ratio*setHeight*app.mathNumber+addY,
                setWidth*(1/3+2*app.mathNumber) + addX+app.mapAdd, setHeight*app.mathNumber+addY,
                setWidth*(1-app.mathNumber) + addX+app.mapAdd, setHeight*(2/3-2*app.mathNumber)+addY,
                setWidth -  ratio*setWidth*app.mathNumber + addX+app.mapAdd, setHeight*(2/3 - (ratio-2)*app.mathNumber)+addY,
                fill = 'Green')
    
    drawPolygon(setWidth*(1-app.mathNumber) + addX+app.mapAdd, setHeight*(2/3-2*app.mathNumber)+addY,
                setWidth + addX+app.mapAdd, setHeight*(2/3-3*app.mathNumber)+addY,
                setWidth + addX+app.mapAdd, addY,
                setWidth*(1/3+3*app.mathNumber) + addX+app.mapAdd, addY,
                setWidth*(1/3+2*app.mathNumber) + addX+app.mapAdd, setHeight*app.mathNumber+addY,
                fill = 'lightBlue')
    drawPolygon(app.mathNumber*setWidth + addX+app.mapAdd, setHeight*(1/3+2*app.mathNumber)+addY,
                addX+app.mapAdd, setHeight*(1/3+3*app.mathNumber)+addY,
                addX+app.mapAdd, setHeight+addY,
                setWidth*(2/3-3*app.mathNumber) + addX+app.mapAdd, setHeight+addY,
                setWidth*(2/3-2*app.mathNumber) + addX+app.mapAdd, setHeight*(1-app.mathNumber)+addY,
                fill = 'lightBlue')

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
    drawLabel(f'You survived {app.timeSurvived} seconds', app.mapWidth/2 + app.mapAdd,
              9*app.mapHeight/16, size = 24)