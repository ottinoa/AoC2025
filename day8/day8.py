import numpy as np
import networkx as nx
import math

INPUT_PATH = "inputs/input.txt"
EDGES_NBR = 10

def _gen_array(filepath):
    """From a file with the vectors separated by newlines and x,y,z separated
        by commas.
    Return a numpy array with the vectors as rows.
    """
    return np.loadtxt(filepath, dtype = 'int', delimiter = ',')

def _connect_closest(array, k = EDGES_NBR):
    """From an array of vectors of unspecified dimension.
    1. Fill an adjacency matrix with the euclidian distance between each vector
        (Calculate only once per pair of vector - undirected graph)
    2. Return the k smallest distances as a list of edges (tuples)
    CAVE : fails if the Kth smallest distance is >9999
    """
    adj_matrix = np.full([array.shape[0], array.shape[0]], 99999999)
    for idx1, vec1 in enumerate(array):
        for idx2, vec2 in enumerate(array[idx1+1:]):
            adj_matrix[idx1,idx2+idx1+1] = np.linalg.norm(vec1-vec2)
    
    #find and return the indices of the k smallest elements with argpartition
    edges = np.argpartition(adj_matrix.ravel(), k)[:k]
    edges = list(zip(*np.unravel_index(edges, adj_matrix.shape)))
    return edges

def _connect_closest_p2(array):
    distances = {} #keys : euclidian distances, values : tuple of vector idx
    boxes_connected = set()
    for idx1, vec1 in enumerate(array):
        for idx2, vec2 in enumerate(array[idx1+1:]):
            distances[np.linalg.norm(vec1-vec2)] = (idx1, idx2+idx1+1)
    
    distances = sorted(distances.items())
    
    for dis,(a,b) in distances:
        boxes_connected.add(a)
        boxes_connected.add(b)
        if len(boxes_connected) == array.shape[0]:
            return a, b #all boxes connected, return the last connected boxes
    

def part_one(input_file):
    a = _gen_array(input_file)
    edges = _connect_closest(a)
    G = nx.Graph(edges)
    
    #Find the unique connected subgraphs and sort them by descending size
    subgraphs = list(nx.connected_components(G))
    subgraphs.sort(key = len, reverse = True)
    
    return math.prod(len(sub) for sub in subgraphs[:3])

def part_two(input_file):
    a = _gen_array(input_file)
    box1, box2 = _connect_closest_p2(a)
    return a[box1,0]*a[box2,0] #multiply x coordinates of last 2 boxes
    
if __name__ == "__main__":
    print("Answer = " + str(part_two(INPUT_PATH)))