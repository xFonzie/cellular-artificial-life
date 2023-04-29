from brain import Brain
import arcade

class Board(arcade.SpriteList):
    def __init__(self, width, height) -> None:
        super().__init__()
        self.matrix = [[Cell() for _ in range(width)] for _ in range(height)]

        self.organisms = []
    
    def generate_board(self, num_organisms):
        for _ in range(num_organisms):
            self.organisms.append(Organism())
        