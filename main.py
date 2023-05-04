from environment.environment import Environment
import numpy as np


def main():
    """ Main function - starting point to the program """
    np.random.seed(0)
    window = Environment()
    window.center_window()
    window.run()


if __name__ == "__main__":
    main()
