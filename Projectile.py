import time

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
    