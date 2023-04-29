from typing import Optional
from arcade import Texture
from brain import Brain
import arcade
from config import ORGANISM_ENERGY, REPRODUCTION_ENERGY

class Organism(arcade.Sprite):
    def __init__(self):
        super().__init__()

        self.brain = Brain()
        self.energy = ORGANISM_ENERGY
        self.age = 0
        self.alive = True

        self.position = (0, 0)
    
    def move_to(self, x, y):
        self.position = (x, y)
    
    def get_action(self, state):
        return self.brain.get_action(state)
    
    def mutate(self, mutation_rate):
        self.brain.mutate(mutation_rate)
    
    def reproduce(self):
        if self.energy < REPRODUCTION_ENERGY:
            return None
        child = Organism()
        child.brain = self.brain
        child.mutate(0.1)
        child.energy = self.energy / 2
        self.energy = self.energy / 2
        return child
    
    def update(self):
        self.age += 1
        self.energy -= 1
        if self.energy <= 0:
            self.alive = False
    
    def get_color(self):
        return self.brain.color