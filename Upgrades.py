from cmu_graphics import *
import random

def sendUpgrade(app):
    index = randrange(0, 3)
    if index == 0 and 'shield' not in app.upgradesList:
        sendShield(app)
    elif index == 1 and 'flash' not in app.upgradesList:
        sendFlash(app)
    elif index == 2 and 'heal' not in app.upgradesList:
        sendHeal(app)

def sendShield(app):
    xCoordinate = randrange(0, app.mapWidth)
    yCoordinate = randrange(0, app.mapHeight)
    for wall in app.walls:
        if wall.collide(app, xCoordinate, yCoordinate):
            xCoordinate = randrange(0, app.mapWidth)
            yCoordinate = randrange(0, app.mapHeight)
    coords = (xCoordinate, yCoordinate)
    app.upgradesList.append(Upgrades('shield', coords))
    print(Upgrades('shield', coords))

def sendFlash(app):
    xCoordinate = randrange(0, app.mapWidth)
    yCoordinate = randrange(0, app.mapHeight)
    for wall in app.walls:
        if wall.collide(app, xCoordinate, yCoordinate):
            xCoordinate = randrange(0, app.mapWidth)
            yCoordinate = randrange(0, app.mapHeight)
    coords = (xCoordinate, yCoordinate)
    app.upgradesList.append(Upgrades('flash', coords))

def sendHeal(app):
    xCoordinate = randrange(0, app.mapWidth)
    yCoordinate = randrange(0, app.mapHeight)
    for wall in app.walls:
        if wall.collide(app, xCoordinate, yCoordinate):
            xCoordinate = randrange(0, app.mapWidth)
            yCoordinate = randrange(0, app.mapHeight)
    coords = (xCoordinate, yCoordinate)
    app.upgradesList.append(Upgrades('heal', coords))

def upgradeCollision(app):
    aliveUpgrades = []
    for upgrade in app.upgradesList:
        x, y = upgrade.coords
        if dist(x, y, app.charX, app.charY) <= app.charSize + upgrade.radius:
            app.activeUpgrade = upgrade.name
        else:
            aliveUpgrades.append(upgrade)
    app.upgradesList = aliveUpgrades

class Upgrades:
    def __init__(self, name, coords):
        self.name = name
        self.coords = coords
        self.radius = 10
    
    def __repr__(self):
        return self.name
    
def dist(x0, y0, x1, y1):
    return ((x1-x0)**2 + (y1-y0)**2)**(1/2)