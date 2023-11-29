def isLegalOneX(app, original, move):
    newX = original + move
    if (app.mapAdd <= newX <= app.mapAdd + 3*app.mapWidth/8 and
        2*app.mapHeight/8 <= app.charY <= 3*app.mapHeight/8):
        return False
    elif (app.mapAdd <= newX <= app.mapAdd + 3*app.mapWidth/8 and
          5*app.mapHeight/8 <= app.charY <= 6*app.mapHeight/8):
        return False
    elif (5*app.mapWidth/8 + app.mapAdd <= newX <= app.mapAdd + app.mapWidth and
          5*app.mapHeight/8 <= app.charY <= 6*app.mapHeight/8):
        return False
    elif (5*app.mapWidth/8  <= newX <= app.mapAdd + app.mapWidth and
          2*app.mapHeight/8 <= app.charY <= 3*app.mapHeight/8):
        return False
    elif newX < 0 or newX > app.mapWidth:
        return False
    return True
    
def isLegalOneY(app, original, move):
    newY = original + move
    if (app.mapAdd <= app.charX <= app.mapAdd + 3*app.mapWidth/8 and
        2*app.mapHeight/8 <= newY <= 3*app.mapHeight/8):
        return False
    elif (app.mapAdd <= app.charX <= app.mapAdd + 3*app.mapWidth/8 and
          5*app.mapHeight/8 <= newY <= 6*app.mapHeight/8):
        return False
    elif (5*app.mapWidth/8 + app.mapAdd <= app.charX <= app.mapAdd + app.mapWidth and
          5*app.mapHeight/8 <= newY <= 6*app.mapHeight/8):
        return False
    elif (5*app.mapWidth/8  <= app.charX <= app.mapAdd + app.mapWidth and
          2*app.mapHeight/8 <= newY <= 3*app.mapHeight/8):
        return False
    elif newY < 0 or newY > app.mapHeight:
        return False
    return True
