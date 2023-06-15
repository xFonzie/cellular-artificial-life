"""
Creation of environment.

Version:
1.0.0

Author:
xFonzie, Zener_085

License:
MIT
"""
import arcade

# pylint: disable=E0402
from .board import Board
from .config import (
    NUM_ORGANISMS,
    SCREEN_HEIGHT,
    SCREEN_TITLE,
    SCREEN_WIDTH,
)


class Environment(arcade.Window):
    """
    Main application class
    """

    def __init__(self):
        """
        Standard constructor for Environment class
        """
        super().__init__(
            SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, update_rate=1 / NUM_ORGANISMS
        )
        self.board = Board()
        self.prev_num_organisms = self.board.get_num_organisms()

    def on_draw(self):
        self.clear()
        self.board.draw()

    def on_update(self, delta_time):
        self.board.update()
        num_orgs = self.board.get_num_organisms()
        if num_orgs:
            self.set_update_rate(1 / self.board.get_num_organisms())
        else:
            print("Everyone is dead")
            self.close()

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.ESCAPE:
            self.close()

    def on_mouse_scroll(self, x: int, y: int, scroll_x: int, scroll_y: int):
        self.board.max_age += scroll_y
        print("new max_age: ", self.board.max_age)
