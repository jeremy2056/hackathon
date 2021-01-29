class player:

    def init(self, life, gold = 0, inventory = set(), level = 0, position):
        self.life = life
        self.gold = gold
        self.inventory = inventory
        self.level = level
        self.position = position
    

class niveau:

    def __init__(self,id, etage, objets, ennemies):
        self.id = id
        self.etage = etage
        self.objets = objets
        self.ennemies = ennemies

class etage:

    def __init__(self,salles, couloirs):
        self.salles = salles
        self.couloirs = couloirs
    
salles = [(0,0,4,5), (7,0,3,4), (11,7,5,2)]
couloirs = [ [(2,5),(2,8),(8,8),(8,4)] , [(4,2),(5,2),(5,1),(6,1)] , [(10,2),(12,2),(12,1),(14,1),(14,6)]]
