from arcade import color

# Set how many rows and columns we will have
ROW_COUNT = 40
COLUMN_COUNT = 40

# This sets the WIDTH and HEIGHT of each grid location
CELL_WIDTH = 8
CELL_HEIGHT = 8

# This sets the margin between each cell
# and on the edges of the screen.
CELL_MARGIN = 0

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
NUM_ORGANISMS = 10
MUTATION_RATE = 0.01

# Organism values
ORGANISM_ENERGY = 50
REPRODUCTION_ENERGY = 50

OBSERVATIONS = ['light-up-left', 'light-up', 'light-up-right', 'light-left', 'light', 'light-right', 'light-down-left', 'light-down', 'light-down-right', 
          'organism-up-left', 'organism-up', 'organism-up-right', 'organism-left', 'organism-right', 'organism-down-left', 'organism-down', 'organism-down-right', 
          'time', 'energy']
ACTIONS = ['up', 'down', 'left', 'right', 'photosynthesis', 'attack', 'reproduce']