# cellular-artificial-life #

This project aims to create a simulation of artificial life using cellular automata and neural
networks. The simulation will allow studying the effects of environmental factors on the evolution
of cells and how different strategies for survival emerge.

---

## Prerequisites ##
To run this simulation, you will need to have Python 3 installed on your system. You will also need
to install the following Python packages:
- [Arcade](https://api.arcade.academy/en/latest/index.html)
- [Numpy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/)
- [Scipy](https://scipy.org/)

You can install these packages using pip by running the following command:
```
pip install --update pip
pip install arcade numpy matplotlib scipy
```

---

## Running the Simulation ##
To run the simulation, you need to execute the `main.py` script:
```
python main.py
```
This will launch the simulation window, where you can observe the artificial life forms evolve.

---

## Simulation Rules ##
The simulation uses a cellular automata model where cells are placed on a grid and interact with
their neighbors based on predefined rules. Cells require energy to live and perform actions, and if
they do not have enough energy, they die and are unable to reproduce.

---

### Observations ###
- Light level
- Other cells (differentiating by species)
- Time of the simulation
- Current energy levels
### Actions ###
- Moving in four directions
- Photosynthesizing
- Eating other cells
- Cloning themselves with some mutations
### Neural Network ###
The simulation uses a neural network to tie observations to actions. The number of neural
connections is limited to simulate biological systems.
### Natural Selection ###
The simulation uses natural selection. Cells with advantageous traits are more likely to survive and
reproduce, passing on their traits to their offspring.

---

## Results ##
Our simulation showed that different strategies for survival emerge based on environmental factors.
In all environments, cells that were able to photosynthesize were more likely to survive and
reproduce. On the other hand, cells that were able to move quickly and consume other cells
were more likely to be killed due to being eaten by its children.

We also observed that mutations played a significant role in the evolution of cells. Mutations that
allowed cells to photosynthesize more efficiently or move more quickly were more likely to be passed
on to offspring.

Furthermore, our simulation provided insights into the behavior of living organisms. We observed
that cells were more likely to consume other cells of the same species rather than different
species, indicating that there may be some level of recognition between cells of the same species.

---

## License ##
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more
information.