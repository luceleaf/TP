import time
import math
from MapDrawings import *

class arrowProjectiles:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.startTime = time.perf_counter()
    
    def getSize(self):
        return self.size
    
    def getStartTime(self):
        return self.startTime
    
    def __repr__(self):
        return (f'''name = {self.name},
                size = {self.size}''')
    

class beamProjectiles:
    def __init__(self, startCoords, playerLocation, mapWidth, mapHeight):
        self.startCoords = startCoords
        self.playerLocation = playerLocation
        x0, y0 = self.startCoords
        x1, y1 = self.playerLocation
        self.slopeY = y1-y0
        self.slopeX = x1-x0
        self.mapWidth = mapWidth
        self.mapHeight = mapHeight
        self.time = 90
        #finds end coords
        x0, y0 = self.startCoords
        xEnd = x0 + self.slopeX
        yEnd = y0 + self.slopeY
        while (0 < xEnd < self.mapWidth or
               0 < yEnd < self.mapHeight):
            xEnd += self.slopeX
            yEnd += self.slopeY
        if xEnd < 0:
            xEnd = 0
            yEnd = y0 + (y1-y0)/(x1-x0)*xEnd
        elif xEnd > self.mapWidth:
            xEnd = self.mapWidth
            yEnd = y0 + (y1-y0)/(x1-x0)*xEnd
        elif yEnd < 0:
            yEnd = 0
            xEnd = y0 + (y1-y0)/(x1-x0)*yEnd
        elif yEnd > self.mapHeight:
            yEnd = self.mapHeight
            xEnd = y0 + (y1-y0)/(x1-x0)*yEnd
        self.endCoords = xEnd, yEnd
        #finds angle
        x0, y0 = self.startCoords
        x1, y1 = self.endCoords
        thetaStart = math.atan2(y0, x0)
        thetaEnd = math.atan2(y1, x1)
        r = (thetaEnd - thetaStart) * (180/math.pi)
        if r < 0:
            r%= 360
        self.angle = r

    def getStartCoords(self):
        return self.startCoords
    
    def getPlayerLocation(self):
        return self.playerLocation
    
    def getTime(self):
        return self.time
    
    def lowerTime(self):
        self.time -= 1

class fishProjectiles:
    def __init__(self, startCoords, endCoords):
        self.startCoords = startCoords
        self.endCoords = endCoords
        self.isAtEnd = False
        self.endTimer = 60

    def getStartCoords(self):
        return self.startCoords
    
    def getEndCoords(self):
        return self.endCoords