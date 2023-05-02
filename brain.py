"""
The Brain class is used to create a neural network that is used to make decisions. It takes in the
size of the input, hidden and output layers, as well as the size of the genome. It provides methods
for creating a random genome, deciphering a genome into weights, getting an action based on a given
input state, mutating the genome, and computing the difference between two brains. It also provides
a visualization method to view the neural network.

Version:
0.0.1

Author:
Smulemun

License:
MIT
"""
# TODO все комменты сгенерировал gpt, поэтому их следует проверить
from copy import deepcopy

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import softmax


# pylint: disable=too-many-instance-attributes
class Brain:
    """
    This is the Brain class for the organism simulation.
    It is used for creating the artificial neural networks for the organism.
    """

    OBSERVATIONS = [
        "light-up-left",
        "light-up",
        "light-up-right",
        "light-left",
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
        "energy"
    ]

    ACTIONS = ["up", "down", "left", "right", "photosynthesis", "attack", "reproduce"]

    # pylint: disable=too-many-arguments
    def __init__(
        self, genome=None, input_size=18, hidden_size=10, output_size=7, size=100
    ):
        """
        Standard constructor for Brain class

        Parameters:
            genome: An optional set of genes that determine the traits of an organism. If not
            provided, the constructor generates a random genome.
            input_size: The number of nodes in the input layer. It represents the number of inputs
            the network expects.
            hidden_size: The number of nodes in the hidden layer.
            output_size: The number of nodes in the output layer. It represents the number of
            outputs the network produces.
            size: The size of the genome if a random one is to be generated. By default, this value
            is set to 100.
        """
        self.input_size = (
            input_size  # 8 light levels, 8 other organisms, 1 time, 1 energy
        )
        self.hidden_size = hidden_size
        self.output_size = (
            output_size  # 4 movement, 1 photosynthesis, 1 attack, 1 reproduction
        )

        if genome is None:
            genome = self.random_genome(size)
        self.genome = genome

        self.weights_layer1 = np.zeros((self.input_size, self.hidden_size))
        self.weights_layer2 = np.zeros((self.hidden_size, self.output_size))
        self.activation1 = np.tanh
        self.activation2 = softmax
        self.decipher()

    def random_genome(self, size: int):
        """
        Generate a random genome of a given size.

        Parameters:
            size: The size of the genome to be generated.

        Returns:
            genome: A list of dictionaries representing the genes. Each dictionary has the following
            keys:
                - layer: An integer representing the layer of the neuron connected to the gene.
                - row: An integer representing the row index of the neuron in the given layer.
                - col: An integer representing the column index of the neuron in the given layer.
                - value: A floating-point number representing the weight of the connection.
        """
        genome = []
        # gene: {"layer": 0-1, "row": int, "col": int, "value": float}
        for _ in range(size):
            gene = {"layer": np.random.randint(0, 2)}
            if gene["layer"] == 0:
                gene["row"] = np.random.randint(0, self.input_size)
                gene["col"] = np.random.randint(0, self.hidden_size)
            elif gene["layer"] == 1:
                gene["row"] = np.random.randint(0, self.hidden_size)
                gene["col"] = np.random.randint(0, self.output_size)
            gene["value"] = np.random.uniform(-1, 1)
            genome.append(gene)
        return genome

    def decipher(self):
        """
        Convert the genome of the organism into the weights of the neural network's connections.
        The method loops over the genome and extracts the values of the genes to update the weights
        of the corresponding connections between input-hidden and hidden-output layers.
        """
        for gene in self.genome:
            if gene["layer"] == 0:
                self.weights_layer1[gene["row"]][gene["col"]] = gene["value"]
            elif gene["layer"] == 1:
                self.weights_layer2[gene["row"]][gene["col"]] = gene["value"]

    def get_action(self, state: list[float]):
        """
        Compute the outputs of the neural network given an input state and return the index of the
        action with the highest predicted value.
        Parameters:
            state: A list of float values representing the current state of the organism.
        Returns:
            index: An integer representing the index of the action with the highest predicted value.
        """
        input_layer = np.array(state)
        hidden_layer = self.activation1(np.dot(input_layer, self.weights_layer1))
        output_layer = self.activation2(np.dot(hidden_layer, self.weights_layer2))
        return output_layer.tolist().index(max(output_layer))

    # pylint: disable=too-many-branches
    def mutate(self, mutation_rate: float):
        """
        Modify the genome of the organism by introducing random mutations at a given mutation rate.
        Parameters:
            mutation_rate: A float value representing the probability of a gene to be mutated.
        Returns:
            mutated_genome: A list of modified genes representing the genome of the mutated
            organism.
        """
        mutated_genome = []
        for gene in self.genome:
            mutated_gene = deepcopy(gene)
            for key in mutated_gene.keys():
                if np.random.uniform(0, 1) < mutation_rate:
                    if key == "layer":
                        mutated_gene[key] = np.random.randint(0, 2)
                        if mutated_gene[key] == 0:
                            mutated_gene["row"] %= self.input_size
                            mutated_gene["col"] %= self.hidden_size
                        elif mutated_gene[key] == 1:
                            mutated_gene["row"] %= self.hidden_size
                            mutated_gene["col"] %= self.output_size
                    elif key == "row":
                        if mutated_gene["layer"] == 0:
                            mutated_gene[key] = np.random.randint(0, self.input_size)
                        elif mutated_gene["layer"] == 1:
                            mutated_gene[key] = np.random.randint(0, self.hidden_size)
                    elif key == "col":
                        if mutated_gene["layer"] == 0:
                            mutated_gene[key] = np.random.randint(0, self.hidden_size)
                        elif mutated_gene["layer"] == 1:
                            mutated_gene[key] = np.random.randint(0, self.output_size)
                    elif key == "value":
                        mutated_gene[key] = np.random.uniform(-1, 1)
            mutated_genome.append(mutated_gene)
        return mutated_genome

    def difference(self, other) -> float:
        """
        Calculate the difference between two organisms' genomes by comparing each gene and key.
        Parameters:
            other: Another organism whose genome is to be compared with the current organism's
            genome.
        Returns:
            difference: A float value representing the difference between the two genomes.
        """
        difference = 0
        for gene1, gene2 in zip(self.genome, other.genome):
            for key in gene1.keys():
                if gene1[key] != gene2[key]:
                    difference += 1
        return difference / (len(self.genome) * 4)

    def genome_color(self) -> list[int]:
        """
        Generate a color code based on the current organism's genome.
        Returns:
            A string representing a color code generated from the current organism's genome.
        """
        color = [0, 0, 0]
        for gene in self.genome:
            if gene["layer"] == 0:
                color[0] += gene["row"] / self.input_size
                color[1] += gene["col"] / self.hidden_size
            elif gene["layer"] == 1:
                color[0] += gene["row"] / self.hidden_size
                color[1] += gene["col"] / self.output_size
            color[2] += (gene["value"] + 1) / 2
        color = [int(c / len(self.genome) * 255) for c in color]
        # pylint: disable=consider-using-f-string
        return color

    def visualize(self):
        """
        Visualize the neural network of the current organism using matplotlib.
        """
        plt.xlim(-2, 4)
        for i in range(self.input_size):
            plt.plot(0, i, "o", color="black")
            plt.text(
                -0.25, i, self.OBSERVATIONS[i], fontsize=8, horizontalalignment="right"
            )
        for i in range(self.hidden_size):
            plt.plot(1, 4 + i, "o", color="black")
        for i in range(self.output_size):
            plt.plot(2, 5 + i, "o", color="black")
            plt.text(2.25, 5 + i, self.ACTIONS[i], fontsize=8)

        for i in range(self.input_size):
            for j in range(self.hidden_size):
                if self.weights_layer1[i][j] != 0:
                    plt.plot(
                        [0, 1],
                        [i, 4 + j],
                        color="blue",
                        linewidth=abs(self.weights_layer1[i][j]) * 2
                    )

        for i in range(self.hidden_size):
            for j in range(self.output_size):
                if self.weights_layer2[i][j] != 0:
                    plt.plot(
                        [1, 2],
                        [4 + i, 5 + j],
                        color="blue",
                        linewidth=abs(self.weights_layer2[i][j]) * 2
                    )

        plt.show()
