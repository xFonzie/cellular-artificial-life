"""
Constants for environment, organism, cells, etc

Version:
1.0.0

Author:
xFonzie

License:
MIT
"""
from time import time
from arcade import color

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


# pylint: disable=invalid-name
def timing(f):
    """
    Wraps the argument function and returns the result of the argument function. It also prints out
    the name of the argument function, the arguments passed to it, the keyword arguments, and the
    time it took to execute the argument function.

    Parameters:
        f: function which is analyzed

    Returns:
        arguments of the function, it's returned value, time the function took to execute
    """
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print(f"func:{f.__name__}, args:[{args[0]}, {args[1]}], took: {kw}, sec: {te - ts}")
        return result

    return wrap
