import numpy as numpy

class player:

    def __init__(self, life, position, gold = 0, level = 0, inventory = set()):
        self.life = life
        self.gold = gold
        self.inventory = inventory
        self.level = level
        self.position = position
    


class niveau:
    def __init__(etage, objets, ennemies, taille):
        self.niveau = [[O for i in range(taille)] for j in range(taille)]
        self.etage = etage
        self.objets = objets
        self.ennemies = ennemies
        self.id = 0

class etage:
    def __init__(salles, couloirs):
        self.salles = salles
        self.couloirs = couloirs
    
salles = [[0,0,3,4], [0, 6, 3, 3]] #deux salles 
test = [[0 for i in range(3)]for j in range(4)]
print(test)