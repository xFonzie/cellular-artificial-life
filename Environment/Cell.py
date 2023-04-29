import arcade
from config import *

class Cell(arcade.SpriteSolidColor):
    def __init__(self, info: dict = None) -> None:
        self.info = {
            'lightlevel': 0,
            'temperature': 0,
            'occupied': None, # Organism
        }

        if info:
            self.info.update(info)
    
    def update(self):
        if self.info['occupied']:
            self.color = arcade.color_from_hex_string(self.info['occupied'].get_color())
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