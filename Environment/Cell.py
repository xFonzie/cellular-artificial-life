

class Cell:
    def __init__(self, **kwargs) -> None:
        self.info = {
            'lightlevel': 0,
            'temperature': 0,
            'occupied': False,
        }

        if kwargs:
            self.info.update(kwargs)
    
    def __getitem__(self, item):
        return self.info[item]
    
    def __setitem__(self, key, value):
        self.info[key] = value
    
    def __repr__(self) -> str:
        return f'<Cell {self.info}>'
    
    def __str__(self) -> str:
        return f'<Cell {self.info}>'