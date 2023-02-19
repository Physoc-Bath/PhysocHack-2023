import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from graphing import graph_coloring_qubo

'''
    Main Page to include the plots we want to minimise. 

    Solution is then solved and plotted through 'graph_coloring_qubo
'''


'''
    Function defining the shapes available to plot, as well as the number of colours
'''

def generate_graph(shape, k):

    print("Visualising the problem we want to solve... \n")

    g = nx.Graph()
    
    # The first problem, goal of the challenge
    if shape == "first problem":

        g.add_edges_from([
                            (0,1),(0,3),(1,3),(1,2)
                        ])
        
    # Hexagonal plot with central point (half plot to save time and memory)
    elif shape == "hexagon centre":
        g.add_edges_from([
                            (0,1),(0,3),(0,4),
                            (1,2),(1,3),
                            (2,3),
                            (3,4)
                        ])
    # Hexagonal plot with no central point
    elif shape == "hexagon no centre":
        g.add_edges_from([
                            (0,1),(0,2),(0,4),(0,5),
                            (1,2),(1,3),(1,5),
                            (2,3),(2,4),
                            (3,5),(3,4),
                            (4,5)
                        ])
        
    # Sqaure with central point
    elif shape == "square central":
        g.add_edges_from([
                            (0,1),(0,2),(0,3),(0,4),
                            (1,2),(1,4),
                            (4,3),
                            (3,2)
                        ])
    # 4 x 2 Grid of points
    elif shape == "4x2 grid":
        g.add_edges_from([
                        (0,4),(0,5),(0,6),(0,7),
                        (1,4),(1,5),(1,6),(1,7),
                        (2,4),(2,5),(2,6),(2,7),
                        (3,4),(3,5),(3,6),(3,7)
                    ])
    else: 
        print("Shape submitted is not recognised!")
        return
    
    nx.draw(g)
    plt.show()
    graph_coloring_qubo(g, k)


generate_graph("hexagon no centre", 3)

