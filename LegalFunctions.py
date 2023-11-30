def isLegalOneX(app, original, move, y):
    newX = original + move
    if (app.mapAdd <= newX <= app.mapAdd + 3*app.mapWidth/8 and
        2*app.mapHeight/8 <= y <= 3*app.mapHeight/8):
        return False
    elif (app.mapAdd <= newX <= app.mapAdd + 3*app.mapWidth/8 and
          5*app.mapHeight/8 <= y <= 6*app.mapHeight/8):
        return False
    elif (5*app.mapWidth/8 + app.mapAdd <= newX <= app.mapAdd + app.mapWidth and
          5*app.mapHeight/8 <= y <= 6*app.mapHeight/8):
        return False
    elif (5*app.mapWidth/8  <= newX <= app.mapAdd + app.mapWidth and
          2*app.mapHeight/8 <= y <= 3*app.mapHeight/8):
        return False
    elif newX < 0 or newX > app.mapWidth:
        return False
    return True

def spawninWall(app, coords):
    x, y = coords
    if (app.mapAdd <= x <= app.mapAdd + 3*app.mapWidth/8 and
        2*app.mapHeight/8 <= y <= 3*app.mapHeight/8):
        return True
    elif (app.mapAdd <= x <= app.mapAdd + 3*app.mapWidth/8 and
          5*app.mapHeight/8 <= y <= 6*app.mapHeight/8):
        return True
    elif (5*app.mapWidth/8 + x <= x <= app.mapAdd + app.mapWidth and
          5*app.mapHeight/8 <= y <= 6*app.mapHeight/8):
        return True
    elif (5*app.mapWidth/8  <= x <= app.mapAdd + app.mapWidth and
          2*app.mapHeight/8 <= y <= 3*app.mapHeight/8):
        return True
    return False
    
def isLegalOneY(app, original, move, x):
    newY = original + move
    if (app.mapAdd <= x <= app.mapAdd + 3*app.mapWidth/8 and
        2*app.mapHeight/8 <= newY <= 3*app.mapHeight/8):
        return False
    elif (app.mapAdd <= x <= app.mapAdd + 3*app.mapWidth/8 and
          5*app.mapHeight/8 <= newY <= 6*app.mapHeight/8):
        return False
    elif (5*app.mapWidth/8 + app.mapAdd <= x <= app.mapAdd + app.mapWidth and
          5*app.mapHeight/8 <= newY <= 6*app.mapHeight/8):
        return False
    elif (5*app.mapWidth/8  <= x <= app.mapAdd + app.mapWidth and
          2*app.mapHeight/8 <= newY <= 3*app.mapHeight/8):
        return False
    elif newY < 0 or newY > app.mapHeight:
        return False
    return True
