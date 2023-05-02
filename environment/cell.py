"""
Class Cell, which represents a single cell on the board
"""
import arcade
# pylint: disable=import-error
from config import CELL_MARGIN, CELL_WIDTH, CELL_HEIGHT, ALIVE_COLOR, DEAD_COLOR


class Cell(arcade.SpriteSolidColor):
    """
    A single cell on the board. Represents what's happening inside of it.
    """
    def __init__(self, x, y, **info: dict):
        """
        Standard constructor for the Cell class

        Parameters:
            x: x coordinate of the cell
            y: y coordinate of the cell
            info: information about this cell (what's inside of it)
        """
        super().__init__(CELL_WIDTH, CELL_HEIGHT, arcade.color.REDWOOD)

        self.center_x = x * (CELL_WIDTH + CELL_MARGIN) + CELL_WIDTH // 2 + CELL_MARGIN
        self.center_y = y * (CELL_HEIGHT + CELL_MARGIN) + CELL_HEIGHT // 2 + CELL_MARGIN

        self.info = {
            "lightlevel": 10,
            "temperature": 0,
            "occupied": None,  # Organism
        }

        if info:
            self.info.update(**info)
    # TODO Зачем переписывать draw() если в нём ничего не поменялось?

    def update(self):
        if self.info["occupied"]:
            self.color = ALIVE_COLOR
        else:
            self.color = DEAD_COLOR

    def __getitem__(self, item):
        return self.info[item]

    def __setitem__(self, key, value):
        self.info[key] = value

    def __repr__(self) -> str:
        return f'<Cell {self.info}>'

    def __str__(self) -> str:
        return f'<Cell {self.info}>'
