from environment.environment import Environment
from environment.config import *
import arcade
import numpy as np

def main():
    """ Main function - starting point to the program """
    np.random.seed(0)
    window = Environment()
    window.center_window()
    arcade.run()

if __name__ == "__main__":
    main()