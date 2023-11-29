import time
import random

class Character:
    def __init__(self, charName, totalHealth, baseSpeed, size, color):
        self.charName = charName
        self.totalHealth = totalHealth
        self.baseSpeed = baseSpeed
        self.size = size
        self.color = color

        self.currSpeed = self.baseSpeed
        self.currHealth = totalHealth
        self.stunTime = 0
        self.slowTime = 0

    def __repr__(self):
        return(f'''name = {self.charName}, 
               total health = {self.totalHealth}, 
               current health = {self.currHealth}, 
               base speed = {self.baseSpeed}, 
               current speed = {self.currSpeed}, 
               size = {self.size}''')
    
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
        self.currHealth -= 75
        self.stunTime = timeinAir ** 0.5

    def fishCollision(self):
        self.currHealth -= 20

teemo = Character('Teemo', 1, 50, 20, 'yellow')
ahri = Character('Ahri', 1500, 40, 20, 'pink')
malphite = Character('Malphite', 3000, 30, 20, 'purple')
