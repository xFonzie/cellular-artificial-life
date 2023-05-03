"""
Class Board, representing the field for organisms.
"""
# pylint: disable=import-error
import random
import math
from organism import Organism
from cell import Cell
import arcade
from config import ROW_COUNT, COLUMN_COUNT, NUM_ORGANISMS


class Board(arcade.SpriteList):
    """
    A board, which represents the field for organisms
    """
    def __init__(self) -> None:
        """
        Standard constructor for the Board class
        """
        super().__init__()
        self.matrix = [[Cell(i, j) for i in range(ROW_COUNT)] for j in range(COLUMN_COUNT)]
        self.time = 0
        self.organisms = []
        self.generate_board()

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
        self.extend(self.organisms)

    def update(self):
        self.time += 0.01
        for org in self.organisms:
            result = org.org_update(self.get_observation(org), self.matrix)

            if result:
                self.organisms.append(result)
                self.matrix[result.pos[0]][result.pos[1]]["occupied"] = result
                self.append(result)

            if not org.alive:
                self.matrix[org.pos[0]][org.pos[1]]["occupied"] = None
                self.organisms.remove(org)
                self.remove(org)

        for row in self.matrix:
            for cell in row:
                cell.update()
        print(self.time)

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
                if i < 0 or i >= ROW_COUNT or j < 0 or j >= COLUMN_COUNT:
                    observation.append(0)
                else:
                    observation.append(self.matrix[i][j]["lightlevel"])

        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if i == x and j == y:
                    continue
                if i < 0 or i >= ROW_COUNT or j < 0 or j >= COLUMN_COUNT:
                    observation.append(None)
                else:
                    observation.append(self.matrix[i][j]["occupied"])

        observation.append(math.sin(self.time))
        print(observation)
        return observation
