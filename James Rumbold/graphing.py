from openqaoa import QAOA  
import networkx as nx
import matplotlib.pyplot as plt
from openqaoa.utilities import ground_state_hamiltonian
from openqaoa.problems import QUBO
from qubo import create_qubo
from colours import bitstring_to_colours, color_map

'''
    Function which takes our graph and number of colours
    and finds the resultant colour plot.
'''
def graph_coloring_qubo(g, k) -> QUBO:
    
    #Generate our QUBO
    gc_qubo = create_qubo(g,k)

    #Initialise model with default configurations
    print("Initialising the model... \n")
    q = QAOA()
    q.compile(gc_qubo)
    q.optimize()
    print("Model created! \n")
    
    #Obtain the optimal results
    opt_results = q.result
    print(f"The optimised results are: \n {opt_results.optimized} \n")
   
    #Plot the Cost History
    opt_results.plot_cost()
    plt.show()

    print(f"The most probable states are: \n {opt_results.most_probable_states} \n")    
        
    #Classical Results
    hamiltonian = gc_qubo.hamiltonian
    energy, configuration = ground_state_hamiltonian(hamiltonian)
    #print(f"Ground State energy: {energy}, Solution: {configuration}")

    #Plot Quantum Results
    solutions_bitstrings = opt_results.most_probable_states['solutions_bitstrings']
    
    solutions = []
    print("Finding the colour scheme for our model... \n")
    for bitstring in solutions_bitstrings:
        solutions.append(bitstring_to_colours( bitstring, k))

    for i, each in enumerate(solutions):

        node_colors = {}
        #For each solution, we use its id and colour index to create our node colours,
        # through the color_map dictionary.
        for idx, color in enumerate(each):
            # Node number = colour matching colour index
            node_colors[idx] = color_map[str(color)]

        nx.draw(g, node_color=[node_colors[node] for node in g.nodes()])
        plt.show()

        if i == 1: break #just show 2 graphs


    return opt_results.optimized['cost']