from Environment.Organism import Organism
from Environment.Cell import Cell
import arcade
import random
from Environment.config import *

class Board(arcade.SpriteList):
    def __init__(self, width, height) -> None:
        super().__init__()
        self.matrix = [[Cell(i, j) for i in range(width)] for j in range(height)]
        self.time = 0
        self.organisms = []

    
    def generate_board(self, num_organisms):
        for _ in range(num_organisms):
            tries = 0
            i, j = random.randint(0, ROW_COUNT - 1), random.randint(0, COLUMN_COUNT - 1)
            while self.matrix[i][j]['occupied']:
                i, j = random.randint(0, ROW_COUNT - 1), random.randint(0, COLUMN_COUNT - 1)
                tries += 1
                assert tries < 1000, 'Too many tries to generate board'
            
            self.organisms.append(Organism(i, j))
            self.matrix[i][j]['occupied'] = self.organisms[-1]
        self.extend(self.organisms)
    
    def update(self):
        self.time += 1
        for org in self.organisms:
            org.update(self.get_observation(org))
            if not org.alive:
                self.matrix[org.pos[0]][org.pos[1]]['occupied'] = None
                self.organisms.remove(org)
                self.remove(org)

        for row in self.matrix:
            for cell in row:
                cell.update()
        print(self.time)


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
                if i == x and j == y:
                    continue
                if i < 0 or i >= ROW_COUNT or j < 0 or j >= COLUMN_COUNT:
                    observation.append(None)
                else:
                    observation.append(self.matrix[i][j]['occupied'])
        
        observation.append(self.time)

        return observation
