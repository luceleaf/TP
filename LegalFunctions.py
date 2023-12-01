def isLegalOneX(app, xc, yc, movex, movey):
    for wall in app.walls:
        posX = xc + movex
        posY = yc + movey
        if wall.collide(app, posX, posY):
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