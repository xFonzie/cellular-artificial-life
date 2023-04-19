class CellState:
    def __init__(self, info=None):
        self.info = {
            'energy': 0,
            'food': 0,
            'poison': 0,
            'wall': False,
            'body': 0,
        }

        if info:
            self.info.update(info)

    def __setitem__(self, key, value):
        self.info[key] = value

    def __getitem__(self, key):
        return self.info[key]

    def update(self, info):
        self.info.update(info)

    def __str__(self):
        return str(self.info)

    def __repr__(self):
        return str(self.info)