

class Board():
    def __init__(self, width, height) -> None:
        self.matrix = [[Cell() for _ in range(width)] for _ in range(height)]

        self.organisms = []