from typing import Optional
from arcade import Texture
from brain import Brain
import arcade
from config import *

class Organism(arcade.SpriteSolidColor):
    def __init__(self, x, y):
        super().__init__()

        self.brain = Brain()
        self.energy = ORGANISM_ENERGY
        self.age = 0
        self.alive = True

        self.position = (x, y)
    
    def kill(self):
        self.alive = False

    def move_to(self, x, y):
        if x < 0 or x >= COLUMN_COUNT or y < 0 or y >= ROW_COUNT:
            return

        self.position = (x, y)

        self.center_x = x * (CELL_WIDTH + CELL_MARGIN) + CELL_WIDTH // 2 + CELL_MARGIN
        self.center_y = y * (CELL_HEIGHT + CELL_MARGIN) + CELL_HEIGHT // 2 + CELL_MARGIN
    
    def reproduce(self):
        if self.energy < REPRODUCTION_ENERGY:
            return None
        child = Organism()
        child.brain.decipher(self.brain.mutate(MUTATION_RATE))
        child.energy = self.energy / 2
        self.energy = self.energy / 2
        return child
    
    def update(self, observation: list):
        self.age += 1
        self.energy -= 1
        if self.energy <= 0:
            self.alive = False
        
        state = [i for i in observation[:9]] +\
                [1 if org else 0 for org in observation[9: 17]] +\
                [observation[17], self.energy]

        action = self.brain.get_action(state)

        if action == 0:
            self.move_to(self.position[0], self.position[1] + 1)
        elif action == 1:
            self.move_to(self.position[0], self.position[1] - 1)
        elif action == 2:
            self.move_to(self.position[0] - 1, self.position[1])
        elif action == 3:
            self.move_to(self.position[0] + 1, self.position[1])
        elif action == 4:
            self.energy += observation[4]
        elif action == 5:
            for i in range(9, 17):
                self.energy += observation[i].energy
                observation[i].kill()
        elif action == 6:
            child = self.reproduce()
            if child is not None:
                return child
        
    def draw(self):
        return super().draw()