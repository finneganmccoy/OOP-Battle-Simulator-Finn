import random
from entity import Entity

class Goblin(Entity):
    def __init__(self, name, health=100, attack_power=15):
        super().__init__(name, health, attack_power)