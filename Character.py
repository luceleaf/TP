import random
from cmu_graphics import *
from PIL import Image

class Character:
    def __init__(self, charName, totalHealth, baseSpeed, size, radius, color):
        self.charName = charName
        self.totalHealth = totalHealth
        self.baseSpeed = baseSpeed
        self.size = size
        self.color = color
        self.currHealth = totalHealth
        self.speed = baseSpeed
        self.stunTime = 0
        self.shieldAmount = 0
        self.timer = 0
        self.invulernable = False
        self.radius = radius
        self.image = CMUImage(Image.open(f'images/{self.charName}.png'))

    def __repr__(self):
        return self.charName
    
    def getCurrentSpeed(self):
        return self.currSpeed
    
    def getCurrentHealth(self):
        return self.currHealth
    
    def getTotalHealth(self):
        return self.totalHealth
    
    def resetCurrentHealth(self):
        self.currHealth = self.totalHealth
    
    def getColor(self):
        return self.color

    def arrowHit(self, timeinAir):
        if self.shieldAmount >= 50:
            self.shieldAmount -= 50
        else:
            self.currHealth += self.shieldAmount - 50
        self.stunTime = int(timeinAir ** 0.5)
        print(self.stunTime)

    def bombCollision(self):
        if self.shieldAmount >= 20:
            self.shieldAmount -= 20
        else:
            self.currHealth += self.shieldAmount - 20

    def karthusHit(self):
        if self.shieldAmount >= 100:
            self.shieldAmount -= 100
        else:
         self.currHealth += self.shieldAmount - 100

    def createShield(self, shieldAmount):
        self.shieldAmount = shieldAmount
        self.timer = 90

    def heal(self):
        self.currHealth += 100
        self.speed *= 2
        self.timer = 90

    def lowerStun(self, app):
        if self.stunTime <= 0:
            self.stunTime = 0
        self.stunTime -= 1

teemo = Character('teemo', 1000, 1.5, 50, 20, 'yellow')
ahri = Character('ahri', 1500, 1, 75, 30, 'pink')
malphite = Character('malphite', 3000, 0.5, 100, 40, 'purple')
