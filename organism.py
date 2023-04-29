import numpy as np

class Organism:

    INITIAL_ENERGY = 5
    ACTION_COSTS = {'up': 1, 'down': 1, 'left': 1, 'right': 1, 'photosynthesis': -5, 'attack': 2, 'reproduce': 10}
    ACTIONS = ['up', 'down', 'left', 'right', 'photosynthesis', 'attack', 'reproduce']

    def __init__(self, x, y, brain):
        self.x = x
        self.y = y
        self.brain = brain
        self.color = brain.genome_to_RGB()
        self.energy = Organism.INITIAL_ENERGY

    def get_action(self, state):
        action = self.brain.get_action(state)
        self.energy -= Organism.ACTION_COSTS[Organism.ACTIONS[action]]
        
        # TODO: implement action
        