import time
import random

class Projectile:
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
    
class Character:
    def __init__(self, charName, totalHealth, baseSpeed, size):
        self.charName = charName
        self.totalHealth = totalHealth
        self.baseSpeed = baseSpeed
        self.size = size

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

    def arrowHit(self):
        self.stunTime = (time.perf_counter() - arrow.getStartTime())*0.5
        self.currHealth -= 75

    def fishHit(self):
        self.currSpeed = self.baseSpeed * 0.85
        self.slowTime = (time.perf_counter() - fish.getStartTime())*.75
        self.currHealth -= fish.getStartTime*20

teemo = Character('Teemo', 1000, 50, .1)
ahri = Character('Ahri', 1500, 40, .15)
malphite = Character('Malphite', 3000, 30, .20)

