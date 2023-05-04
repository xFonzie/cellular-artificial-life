"""
Constants for environment, organism, cells, etc
"""
from arcade import color
from time import time

# Set how many rows and columns we will have
ROW_COUNT = 100
COLUMN_COUNT = 100

# This sets the WIDTH and HEIGHT of each grid location
CELL_WIDTH = 3
CELL_HEIGHT = 3

# This sets the margin between each cell
# and on the edges of the screen.
CELL_MARGIN = 2

# Do the math to figure out our screen dimensions
SCREEN_WIDTH = (CELL_WIDTH + CELL_MARGIN) * COLUMN_COUNT + CELL_MARGIN
SCREEN_HEIGHT = (CELL_HEIGHT + CELL_MARGIN) * ROW_COUNT + CELL_MARGIN
SCREEN_TITLE = "Window"

# Colors and alpha values
ALIVE_COLOR = color.BISTRE
DEAD_COLOR = color.BLACK
BACKGROUND_COLOR = color.ANTIQUE_WHITE
ALPHA_ON = 255
ALPHA_OFF = 0

# Set the number of organisms
NUM_ORGANISMS = 500
MUTATION_RATE = 0.01

# Organism values
ORGANISM_ENERGY = 10
REPRODUCTION_ENERGY = 20
MAX_AGE = 15

OBSERVATIONS = [
    "light-up-left",
    "light-up",
    "light-up-right",
    "light-left",
    "light",
    "light-right",
    "light-down-left",
    "light-down",
    "light-down-right",
    "organism-up-left",
    "organism-up",
    "organism-up-right",
    "organism-left",
    "organism-right",
    "organism-down-left",
    "organism-down",
    "organism-down-right",
    "time",
    "energy"]

ACTIONS = ["up", "down", "left", "right", "photosynthesis", "attack"]

def timing(f):
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print('func:%r args:[%r, %r] took: %2.4f sec' % \
              (f.__name__, args, kw, te - ts))
        return result

    return wrap
