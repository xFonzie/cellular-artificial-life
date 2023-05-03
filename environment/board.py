"""
Class Board, representing the field for organisms.
"""
# pylint: disable=import-error
import random
import math
from environment.organism import Organism
from environment.cell import Cell
import arcade
from environment.config import ROW_COUNT, COLUMN_COUNT, NUM_ORGANISMS


class Board(arcade.SpriteList):
    """
    A board, which represents the field for organisms
    """
    def __init__(self) -> None:
        """
        Standard constructor for the Board class
        """
        super().__init__()
        self.matrix = [[Cell(i, j, 
                            #  lightlevel = ROW_COUNT // 2 - abs(ROW_COUNT // 2 - i) + COLUMN_COUNT // 2 - abs(COLUMN_COUNT // 2 - j)
                            # lightlevel = int(50 / math.sqrt((ROW_COUNT // 2 - i) ** 2 + (COLUMN_COUNT // 2 - j) ** 2 + 1)),
                             ) for i in range(ROW_COUNT)] for j in range(COLUMN_COUNT)]
        self.time = 0
        self.organisms = []
        self.generate_board()

        # tmp
        self.day_rows = range(0, 11)

    def generate_board(self):
        """
        Generation multiple cells with organisms
        """
        for _ in range(NUM_ORGANISMS):
            tries = 0
            i, j = random.randint(0, ROW_COUNT - 1), random.randint(0, COLUMN_COUNT - 1)
            while self.matrix[i][j]["occupied"]:
                i, j = random.randint(0, ROW_COUNT - 1), random.randint(0, COLUMN_COUNT - 1)
                tries += 1
                assert tries < 1000, "Too many tries to generate board"  # TODO а это зачем?

            self.organisms.append(Organism(i, j))
            self.matrix[i][j]["occupied"] = self.organisms[-1]
            # print(self.organisms[-1].color)
        self.extend(self.organisms)

    def update(self):
        self.time += 0.01

        children = []

        for org in self.organisms:
            result = org.org_update(self.get_observation(org), self.matrix)

            if result:
                children.append(result)

            if not org.alive or org.energy <= 0:
                self.matrix[org.pos[0]][org.pos[1]]["occupied"] = None
                self.organisms.remove(org)
                self.remove(org)

        for child in children:
            if self.matrix[child.pos[0]][child.pos[1]]["occupied"] is None:
                self.organisms.append(child)
                self.matrix[child.pos[0]][child.pos[1]]["occupied"] = child
                self.append(child)

        for row in self.matrix:
            for cell in row:
                cell.update()

        if int(self.time * 100) % 10 == 0:
            for x in range(len(self.matrix)):
                if x in self.day_rows:
                    for y in range(len(self.matrix[x])):
                        self.matrix[x][y]['lightlevel'] = 7
                else:
                    for y in range(len(self.matrix[x])):
                        self.matrix[x][y]['lightlevel'] = 0

            self.day_rows = [(row + 1) % COLUMN_COUNT for row in self.day_rows]

        # print(self.time)
        if len(self.organisms) > 0:
            print(f'Population: {len(self.organisms)}. Average energy: {sum([org.energy for org in self.organisms]) / len(self.organisms)}. Day: {self.day_rows}')

    def get_observation(self, organism: Organism):
        """
        Getting information about cells around for organism

        Parameters:
            organism: a single organism

        Returns:
            an observation, describing light level in the cells, occupied cells around and time
            spent
        """
        # pylint: disable=invalid-name
        x, y = organism.pos
        observation = []
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                new_x, new_y = i, j
                if new_x < 0:
                    new_x = ROW_COUNT - 1
                if new_x >= ROW_COUNT:
                    new_x = 0
                if new_y < 0:
                    new_y = COLUMN_COUNT - 1
                if new_y >= COLUMN_COUNT:
                    new_y = 0
                observation.append(self.matrix[new_x][new_y]["lightlevel"])

        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if i == x and j == y:
                    continue
                new_x, new_y = i, j
                if new_x < 0:
                    new_x = ROW_COUNT - 1
                if new_x >= ROW_COUNT:
                    new_x = 0   
                if new_y < 0:
                    new_y = COLUMN_COUNT - 1
                if new_y >= COLUMN_COUNT:
                    new_y = 0
                observation.append(self.matrix[new_x][new_y]["occupied"])

        observation.append(math.sin(self.time))
        return observation
