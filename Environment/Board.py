from Organism import Organism
import arcade
import random
from config import *

class Board(arcade.SpriteList):
    def __init__(self, width, height) -> None:
        super().__init__()
        self.matrix = [[Cell() for _ in range(width)] for _ in range(height)]

        self.organisms = []

    
    def generate_board(self, num_organisms):
        for _ in range(num_organisms):
            tries = 0
            i, j = random.randint(0, ROW_COUNT - 1), random.randint(0, COLUMN_COUNT - 1)
            while self.matrix[i][j]['occupied']:
                i, j = random.randint(0, ROW_COUNT - 1), random.randint(0, COLUMN_COUNT - 1)
                tries += 1
                assert tries < 1000, 'Too many tries to generate board'
            
            self.organisms.append(Organism())
            self.matrix[i][j]['occupied'] = self.organisms[-1]
            self.append(self.organisms[-1])
    
    def update(self):
        for org in self.organisms:
            org.update(self.get_observation(org))
            if not org.alive:
                self.matrix[org.position[0]][org.position[1]]['occupied'] = None
                self.organisms.remove(org)
                self.remove(org)

        for row in self.matrix:
            for cell in row:
                cell.update()
    
    def get_observation(self, organism):
        x, y = organism.position
        observation = []
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if i < 0 or i >= ROW_COUNT or j < 0 or j >= COLUMN_COUNT:
                    observation.append(0)
                else:
                    observation.append(self.matrix[i][j]['lightlevel'])
        
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if i < 0 or i >= ROW_COUNT or j < 0 or j >= COLUMN_COUNT:
                    observation.append(None)
                else:
                    observation.append(self.matrix[i][j]['occupied'])
        
        observation.append(organism.energy)
        return observation
    
    def draw(self):
        for row in self.matrix:
            for cell in row:
                cell.draw()