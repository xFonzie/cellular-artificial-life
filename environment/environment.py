"""
Creation of environment.
"""
import arcade
# pylint: disable=import-error
from environment.config import BACKGROUND_COLOR, SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, UPDATE_RATE
from environment.board import Board


# import random


class Environment(arcade.Window):
    """
    Main application class
    """

    def __init__(self):
        """
        Standard constructor for Environment class
        """
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, update_rate=UPDATE_RATE)

        self.background_color = BACKGROUND_COLOR

        self.board = Board()

    def on_draw(self):
        self.clear()
        self.board.draw()

    def on_update(self, delta_time):
        self.board.update()

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.ESCAPE:
            self.close()
