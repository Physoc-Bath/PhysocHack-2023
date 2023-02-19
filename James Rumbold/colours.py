import numpy as np

#Colours used for the plot, taken from known solution

color_map = {   
    '0': 'blue', 
    '1': 'red', 
    '2': 'green',
    '3': 'orange',
    '4': 'purple',
    '5': 'brown',
    '6': 'pink',
    '7': 'gray',
    '8': 'olive',
    '9': 'cyan', 
    'x': 'black'}

'''
    Converting our bitstrings in binary to our colours, noting that one node has k bits, with the bit = 1 
    corresponding to the colour of our ndoe.
'''

def bitstring_to_colours(bitstring, k):

        # The colours array for each node in our plot
        colours = []

        # If the bitstring is not divisible by k, return
        if ( np.mod( len(bitstring) , k ) != 0):
            print("Bitstring must be divisible by k!")
            return
        
        # Find the binary colours associated with each node
        for i in range ( 0, len(bitstring), k ):

            node_i = bitstring[i:i+k]

            if "1" in node_i:
                for j in range(k):

                    #Find which colour is associated with this node
                    if node_i.index('1') == j:
                        colours.append(j)

            #If this node has no 1 bits
            else:
                colours.append("x")                    

        return colours