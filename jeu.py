class player:

    def init(self, life, gold = 0, inventory = set(), level = 0, position):
        self.life = life
        self.gold = gold
        self.inventory = inventory
        self.level = level
        self.position = position
    


class niveau(etage, objets, ennemies):
    self.etage = etage
    self.objets = objets
    self.ennemies = ennemies

class etage(salles, couloirs):
    self.salles = salles
    self.couloirs = couloirs