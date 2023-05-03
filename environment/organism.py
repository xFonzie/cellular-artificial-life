"""
Description of the Organism class
"""

from typing import Optional
# from arcade import Texture
import arcade
# pylint: disable=import-error
from environment.config import (
    CELL_HEIGHT,
    CELL_MARGIN,
    CELL_WIDTH,
    ORGANISM_ENERGY,
    MUTATION_RATE,
    COLUMN_COUNT,
    ROW_COUNT,
    REPRODUCTION_ENERGY,
)
from environment.brain import Brain
from environment.cell import Cell
import random


class Organism(arcade.SpriteSolidColor):
    """
    Organism is a single entity that tries to survive in te environment.
    """
    brain = ...

    def __init__(self, x: int, y: int, parent: Optional["Organism"] = None):
        """
        Standard constructor for the Organism class

        Parameters:
            x: x coordinate of the organism
            y: y coordinate of the organism
            parent: a parent of the organism
        """
        self.brain = Brain(genome=parent.brain.mutate(MUTATION_RATE) if parent else None, size=50)
        super().__init__(CELL_WIDTH, CELL_HEIGHT, self.brain.genome_color())
        self.color = self.brain.genome_color()
        self.energy = ORGANISM_ENERGY
        self.age = 0
        self.alive = True

        self.center_x = x * (CELL_WIDTH + CELL_MARGIN) + CELL_WIDTH // 2 + CELL_MARGIN
        self.center_y = y * (CELL_HEIGHT + CELL_MARGIN) + CELL_HEIGHT // 2 + CELL_MARGIN

        self.pos = x, y  # TODO если ты уже поменял центр координат, зачем обновлять pos?

    def kill(self):
        self.alive = False

    # pylint: disable=invalid-name
    def __move_to(self, x: int, y: int, matrix: list[list[Cell]]):
        """
        The organism moves to another cell

        Parameters:
            x: x coordinate of the cell the organism should move
            y: y coordinate of the cell the organism should move
            matrix: matrix with all cells for checking if the organism wants to move to another
                organism
        """

        if x < 0:
            x = COLUMN_COUNT - 1
        elif x >= COLUMN_COUNT:
            x = 0
        if y < 0:
            y = ROW_COUNT - 1
        elif y >= ROW_COUNT:
            y = 0

        if matrix[x][y]["occupied"]:
            return

        # if x < 0 or x >= COLUMN_COUNT or y < 0 or y >= ROW_COUNT:

        matrix[self.pos[0]][self.pos[1]]["occupied"] = None
        self.pos = x, y
        matrix[x][y]["occupied"] = self

        self.center_x = x * (CELL_WIDTH + CELL_MARGIN) + CELL_WIDTH // 2 + CELL_MARGIN
        self.center_y = y * (CELL_HEIGHT + CELL_MARGIN) + CELL_HEIGHT // 2 + CELL_MARGIN

    def __reproduce(self, matrix: list[list[Cell]]):
        """
        The organism makes a child
        """
        if self.energy <= REPRODUCTION_ENERGY:
            return None
        child_x, child_y = self.pos
        posible_cells = []
        for x in range(child_x - 1, child_x + 2):
            for y in range(child_y - 1, child_y + 2):
                new_x, new_y = x, y
                if new_x < 0:
                    new_x = COLUMN_COUNT - 1
                elif new_x >= COLUMN_COUNT:
                    new_x = 0
                if new_y < 0:
                    new_y = ROW_COUNT - 1
                elif new_y >= ROW_COUNT:
                    new_y = 0
                if not matrix[new_x][new_y]["occupied"]:
                    posible_cells.append((new_x, new_y))

        if not posible_cells:
            return None
        child_x, child_y = random.choice(posible_cells)
        child = Organism(child_x, child_y, parent=self)
        child.energy = self.energy // 2
        self.energy = self.energy // 2
        # self.energy -= REPRODUCTION_ENERGY
        return child

    # TODO update() переписывается с другими аргументами
    def org_update(self, observation: list, matrix: list[list[Cell]]) -> Optional["Organism"]:
        """
        The organism makes a step

        Parameters:
            observation: list of data represented cells and organisms around
            matrix: matrix with all cells in the environment

        Returns:
            A child if it's created, otherwise None
        """
        
        # self.age += 1
        self.energy -= 1
        if self.energy <= 0 or self.age > 8:
            self.kill()
            return None

        state = (
                list(observation[:9]) + 
                [self.brain.difference(org.brain) if org else 0 for org in observation[9: 17]] +
                [observation[17], self.energy]
        )

        action = self.brain.get_action(state)

        match action:
            case 0:
                self.__move_to(self.pos[0], self.pos[1] + 1, matrix)
            case 1:
                self.__move_to(self.pos[0], self.pos[1] - 1, matrix)
            case 2:
                self.__move_to(self.pos[0] - 1, self.pos[1], matrix)
            case 3:
                self.__move_to(self.pos[0] + 1, self.pos[1], matrix)
            case 4:
                self.energy += observation[4]
                # print(f'ate at {self.pos} with {observation[4]} energy')
            case 5:
                for i in range(9, 17):
                    if observation[i] is not None and observation[i].alive:
                        self.energy += observation[i].energy
                        observation[i].kill()
                        # print(f'killed at {observation[i].pos} by {self.pos}')
            # case 6:
            #     child = self.__reproduce(matrix)
            #     if child is not None:
            #         return child   

        if self.energy > REPRODUCTION_ENERGY:
            child = self.__reproduce(matrix)
            if child is not None:
                return child
        
        return None
