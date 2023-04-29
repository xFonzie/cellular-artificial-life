import arcade
from Environment.config import *
from Environment.Board import Board
import random

class Environment(arcade.Window):
    """
    Main application class
    """

    def __init__(self, width: int = 800, height: int = 600, title: str | None = 'Arcade Window', 
                 fullscreen: bool = False, resizable: bool = False, update_rate: float | None = 1 / 60):
        
        super().__init__(width, height, title, fullscreen, resizable, update_rate)
        
        self.background_color = BACKGROUND_COLOR

        self.board = Board(ROW_COUNT, COLUMN_COUNT)
        self.board.generate_board(NUM_ORGANISMS)

    
    def on_draw(self):
        """
        Render the screen.
        """
        arcade.start_render()
        self.board.draw()
    
    def on_update(self, delta_time):
        self.board.update()
    
    def on_key_press(self, key, modifiers):
        pass