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
    
salles = [(0,0,4,5), (7,0,3,4), (11,7,5,2)]
couloirs = [ [(2,5),(2,8),(8,8),(8,4)] , [(4,2),(5,2),(5,1),(6,1)] , [(10,2),(12,2),(12,1),(14,1),(14,6)]]
test = [[0 for i in range(3)]for j in range(4)]
print(test)
