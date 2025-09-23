
import random
import matplotlib.pyplot as plt
import math

class Alien:
    
    def __init__(self):
        self.age = 1
        self.isAlive = True
        
    def birthday(self):
        self.age+=1
        
    def considerDying(self):
        if random.randint(0,10) < self.age:
            self.isAlive = False
            
    def reproduce(self):
        return self.isAlive and random.randint(0,6) > self.age


aliens = [Alien()]
timeSeries = []
            
for i in range(100):

    
    aliensToAdd = 0
    
    for alien in aliens:
        alien.birthday()
        if alien.reproduce():
            aliensToAdd+=1
        alien.considerDying()
        
    aliens = [x for x in aliens if x.isAlive]
    
    for new in range(aliensToAdd):
        aliens.append(Alien())
        
    timeSeries.append(len(aliens))
    
x = list(range(100))
y = timeSeries





import math

def perimeter_calc(radius):
    try:
        assert isinstance(radius, (int, float)) and radius >= 0
        return math.pi * 2 * radius
    except AssertionError:
        print("invalid input")
         # return explicitly
    

print(perimeter_calc('l'))  # prints "invalid input" and returns None
print(perimeter_calc(5))    # 31.41592653589793
