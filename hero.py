from entity import Entity

class Hero(Entity):
    def __init__(self, name, health=200):
        super().__init__(name, health= health, attack_power= 50)
    def superAttack(self):
        return 9999