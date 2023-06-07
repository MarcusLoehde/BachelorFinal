# importing module
import sys
# appending a path
sys.path.append('TestSuite')
import random
import matplotlib.pyplot as plt
import Sequences.SequenceGetter as sg


class random_modulo_prime:    
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.large_prime = 101
        self.x = 0

    def __next__(self, range):
        r = (self.a*self.x+self.b) % self.large_prime
        self.x += 1
        return r % (range + 1)

    def __new_seed__(self, a, b):
        self.a = a
        self.b = b

random_m = random_modulo_prime(8328, 3883)


true_random_sequence = sg.getTrulyRandomBits()

true_random_sequence_seeds = sg.getTrulyRandomSeed_101()


def true_random():
    return true_random_sequence.pop(0)

    

def random_source(source):
    if source == "python":
        return random.randint(0,1)
    elif (source == "true"):
        return true_random()
    else:
        return random_m.__next__(1)



class Node:
    def __init__(self, id, rand_mode):
        self.id = id
        self.neighbors = set()
        self.color = random_source(rand_mode)


def test_maxcut_approx(num_nodes, num_edges, a, b, rand_mode):

    random_m.__new_seed__(a, b)

    # Create a list of nodes
    nodes = [Node(i, rand_mode) for i in range(num_nodes)]

    # Create randomm edges edges between nodes
    i = 0
    while(i < num_edges):
        rand_node1 = random.randint(0, num_nodes-1)
        rand_node2 = random.randint(0, num_nodes-1)
        if(rand_node1 != rand_node2 and not nodes[rand_node1].neighbors.__contains__(rand_node2) and not nodes[rand_node2].neighbors.__contains__(rand_node1)):
            nodes[rand_node1].neighbors.add(rand_node2)
            nodes[rand_node2].neighbors.add(rand_node1)
            i += 1

    #calculate the amount of edges cut
    cut = 0
    for node in nodes:
        if node.color == 0:
            for n in node.neighbors:
                if(nodes[n].color == 1):
                    cut += 1
    return cut



def get_rand_seed_101(zero=True):
    r = 0
    #if zero true we filter out zeros
    if zero:
        while r == 0:
            r = true_random_sequence_seeds.pop(0)
        return r
    else:
        r = true_random_sequence_seeds.pop(0)
        return r


def __main__():
    result = []
    
    num_edges = 1000
    num_nodes = 100
    #Can't have more edges if all nodes are connected already
    if num_edges > (num_nodes-1)*num_nodes/2:
        num_edges = (num_nodes-1)*num_nodes/2
    
    # Specify the number of tests
    num_tests = 1000

    #Set seed so comparison is valid
    random.seed(42069)
    for i in range(num_tests):
        result.append(test_maxcut_approx(num_nodes, num_edges, get_rand_seed_101(zero=True), get_rand_seed_101(), "modulo"))
    average = sum(result)/num_tests
    print("Average with pairwise independence: ", average)
    print("Variance: ", (1/num_tests)*sum([((r-average)**2) for r in result]))
    print("------------------------------------------------")
    random.seed(42069)
    result2 = []
    for i in range(num_tests):
        result2.append(test_maxcut_approx(num_nodes, num_edges, 0, 0, "true"))
    average = sum(result2)/num_tests
    print("Average with independence: ", average)
    print("Variance: ", (1/num_tests)*sum([((r-average)**2) for r in result2]))


    # Determine the interval around expected we see in histogram
    interval = 50

    # Plot histogram for results
    plt.hist(result, bins=100, alpha=0.5, label='Results of MaxCut from pairwise independence', range=(num_edges/2-interval,num_edges/2+interval))
    plt.xlabel('Edges Cut')
    plt.ylabel('Frequency of edges cut in MaxCut')
    plt.title('Histogram of 1000 MaxCut runs')
    plt.grid(True)

    
    # Plot histogram for results2
    plt.hist(result2, bins=100, alpha=0.5, label='Results of MaxCut from true randomness', range=(num_edges/2-interval,num_edges/2+interval))
   
    # Display legend
    plt.legend()

    # Show the plot
    plt.show()



if __name__ == "__main__":
    __main__()


