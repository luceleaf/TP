import time
import random

class Projectile:
    def __init__(self, name, size, effect):
        self.name = name
        self.size = size
        self.startTime = time.perf_counter()
        self.effect = effect
    
    def getSize(self):
        return self.size
    
    def getEffect(self):
        return self.effect
    
    def getStartTime(self):
        return self.startTime
    
    def __repr__(self):
        return (f'''name = {self.name},
                size = {self.size}''')
    
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

    def arrowHit(self, startTime):
        self.currHealth -= 75
        self.stunTime = (int(time.time()) - startTime)**0.5

    def fishHit(self):
        self.currSpeed = self.baseSpeed * 0.85
        self.slowTime = (int(time.time()) - fish.getStartTime())*.75
        self.currHealth -= fish.getStartTime*20

teemo = Character('Teemo', 1, 50, .1, 'yellow')
ahri = Character('Ahri', 1500, 40, .15, 'pink')
malphite = Character('Malphite', 3000, 30, .20, 'purple')
