import numpy as np
from openqaoa.problems import QUBO

'''
    Function which finds our Q matrix and therefore our QUBO
'''

def create_qubo(g,k):
    print("Generating the QUBO for our problem.... \n")

    #Set up Qubo-Problem
    A = 10
    n_nodes = g.number_of_nodes()
    num_vertices = k * n_nodes

    #Generate Q Matrix
    Q_matrix = np.zeros((num_vertices, num_vertices))

    # Add terms where i = j and u != v
    for u,v in g.edges():
        k_vals = np.arange(0, k, 1)
 
        for i in k_vals:
            Q_matrix[u*k+i][v*k+i] += A
            Q_matrix[v*k+i][u*k+i] += A

    # Add terms where i = j and u=v
    for u in g.nodes():
        k_vals = np.arange(0, k, 1)
        for i in k_vals:
            Q_matrix[u*k+i][u*k+i] -= A

    # Add terms where i != j and u = v
    for u in g.nodes():
        k_vals = np.arange(0, k, 1)
        for i in k_vals:
            j_vals = np.setdiff1d(k_vals, [i])
            for j in j_vals:
                Q_matrix[u*k+i][u*k+j] += A

    # Transform Q to J and h 
    J_matrix = np.zeros(( num_vertices , num_vertices ))
    h_list = np.zeros( num_vertices )

    for i in range( num_vertices ):

        sum_Qij = 0

        for j in range( num_vertices):
            if (j != i ):
                J_matrix[i][j] = Q_matrix[i][j]/4
                J_matrix[j][i] = Q_matrix[j][i]/4

                sum_Qij += Q_matrix[i][j]

        h_list[i] = -0.5 * Q_matrix[i][i] - 0.25 * sum_Qij

    #Create the terms and weights array
    terms = []
    weights = []

    for i in range( num_vertices ):
        terms.append([i])
        weights.append(h_list[i])

        for j in range( num_vertices ):

            if ( J_matrix[i][j] != 0):
                terms.append([i,j])
                weights.append(J_matrix[i][j])

    
    qubo_problem = QUBO(terms=terms, weights=weights, n=num_vertices)

    print("QUBO created! \n")
    
    return qubo_problem