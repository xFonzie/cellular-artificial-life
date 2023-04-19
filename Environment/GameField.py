from Environment.CellState import CellState
import pygame

class GameField:
    def __init__(self, board_size:tuple) -> None:
        self.width = board_size[0]
        self.height = board_size[1]

        self.board = [[CellState() for _ in range(self.width)] for _ in range(self.height)]
    

class GameFieldRenderer():
    def __init__(self, gamefield, screen) -> None:
        pass