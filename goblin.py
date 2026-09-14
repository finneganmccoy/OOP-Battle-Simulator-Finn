import random
from character import Character

class Goblin(Character):
    def __init__(self, name="Hero"):
        self.name = name
        self.health = 100
        self.attack_power = 50