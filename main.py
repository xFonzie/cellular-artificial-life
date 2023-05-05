"""
Main file of the project. Used for running only.
"""
import numpy as np

# pylint: disable=import-error
from environment.environment import Environment


def main():
    """
    Main function - starting point to the program
    """
    np.random.seed(0)
    window = Environment()
    window.center_window()
    window.run()


if __name__ == "__main__":
    main()
