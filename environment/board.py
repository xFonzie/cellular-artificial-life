"""
Class Board, representing the field for organisms.

Version:
1.0.0

Author:
xFonzie

License:
MIT
"""
import math

import random

import arcade

# pylint: disable=E0402
from .cell import Cell
from .config import COLUMN_COUNT, MAX_AGE, NUM_ORGANISMS, ROW_COUNT
from .organism import Organism


class Board(arcade.SpriteList):
    """
    A board, which represents the field for organisms
    """

    def __init__(self) -> None:
        """
        Standard constructor for the Board class
        """
        super().__init__()
        self.matrix = [
            [
                Cell(
                    i,
                    j,
                    lightlevel=70
                    / math.sqrt(
                        (ROW_COUNT // 2 - i) ** 2 + (COLUMN_COUNT // 2 - j) ** 2 + 1
                    ),
                )
                for i in range(ROW_COUNT)
            ]
            for j in range(COLUMN_COUNT)
        ]
        self.time = 0
        self.organisms: list[Organism] = []
        self.generate_board()
        self.max_age = MAX_AGE
        # tmp
        self.day_rows = list(range(0, 11))
        self.__num_organisms = NUM_ORGANISMS

    def generate_board(self):
        """
        Generation multiple cells with organisms
        """
        for _ in range(NUM_ORGANISMS):
            tries = 0
            i, j = random.randint(0, ROW_COUNT - 1), random.randint(0, COLUMN_COUNT - 1)
            while self.matrix[i][j]["occupied"]:
                i, j = random.randint(0, ROW_COUNT - 1), random.randint(
                    0, COLUMN_COUNT - 1
                )
                tries += 1
                assert tries < 1000, "Too many tries to generate board"

            self.organisms.append(Organism(i, j))
            self.matrix[i][j]["occupied"] = self.organisms[-1]
            # print(self.organisms[-1].color)
        self.extend(self.organisms)

    def get_num_organisms(self):
        """
        Returns number of organisms on the board

        Returns:
            number of organisms on the board
        """
        return self.__num_organisms

    def update(self):
        self.time += 0.01

        children = []

        for org in self.organisms:
            result = org.org_update(
                self.get_observation(org), self.matrix, self.max_age
            )

            if result:
                children.append(result)
                self.__num_organisms += 1

            if not org.alive or org.energy <= 0:
                self.matrix[org.pos[0]][org.pos[1]]["occupied"] = None
                self.organisms.remove(org)
                org.kill()
                self.__num_organisms -= 1
                try:
                    self.atlas.remove(org.texture)
                except ValueError:
                    pass

        for child in children:
            if self.matrix[child.pos[0]][child.pos[1]]["occupied"] is None:
                self.organisms.append(child)
                self.matrix[child.pos[0]][child.pos[1]]["occupied"] = child
                self.append(child)

        for row in self.matrix:
            for cell in row:
                cell.update()

        if int(self.time * 100) == 500:
            # pylint: disable=invalid-name
            n = 0
            for org in self.organisms:
                org.brain.save_genome(f"brains/brain{n}.json")
                n += 1

    @staticmethod
    def __update_coordinates(__i: int, __j: int) -> tuple[int, int]:
        """
        Creates new coordinates for observing cells around

        Parameters:
            __i: each x coordinate of cells around
            __j: each y coordinate of cells around

        Returns:
            New coordinates describing each cell around
        """
        new_x, new_y = __i, __j
        if new_x < 0:
            new_x = ROW_COUNT - 1
        if new_x >= ROW_COUNT:
            new_x = 0
        if new_y < 0:
            new_y = COLUMN_COUNT - 1
        if new_y >= COLUMN_COUNT:
            new_y = 0
        return new_x, new_y

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
                new_x, new_y = self.__update_coordinates(i, j)
                observation.append(self.matrix[new_x][new_y]["lightlevel"])

        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if i == x and j == y:
                    continue
                new_x, new_y = self.__update_coordinates(i, j)
                observation.append(self.matrix[new_x][new_y]["occupied"])

        observation.append(math.sin(self.time))
        return observation
