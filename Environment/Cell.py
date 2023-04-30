import arcade
from Environment.config import *

class Cell(arcade.SpriteSolidColor):
    def __init__(self, x, y, info: dict = None) -> None:
        super().__init__(CELL_WIDTH, CELL_HEIGHT, arcade.color.REDWOOD)

        self.center_x = x * (CELL_WIDTH + CELL_MARGIN) + CELL_WIDTH // 2 + CELL_MARGIN
        self.center_y = y * (CELL_HEIGHT + CELL_MARGIN) + CELL_HEIGHT // 2 + CELL_MARGIN

        self.info = {
            'lightlevel': 10,
            'temperature': 0,
            'occupied': None, # Organism
        }
        
        if info:
            self.info.update(info)
    
    def draw(self):
        super().draw()

    def update(self):
        if self.info['occupied']:
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