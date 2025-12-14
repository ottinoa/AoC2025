INPUT_PATH = "inputs/input.txt"

def _adjacency_list(path=INPUT_PATH):
    with open(path, 'r') as f:
        lines = f.read().splitlines()
        adj_list = {}
        for line in lines:
            key = line.split(':')[0]
            vals = line.split(':')[1].split()
            adj_list[key] = vals
    return adj_list

def _topological_sort(G):
    """Simple depth-first method to return the node keys in topological order
    Input : adjacency list as a dict.
    Output : list of node keys.
    CAVE: only works on acyclic graphs."""
    visited = set()
    order = []
    def visit(node):
        visited.add(node)
        for neighbour in G[node]:
            if neighbour not in visited:
                visit(neighbour)
        order.append(node)
    for node in G.keys():
        if node not in visited:
            visit(node)
    return list(reversed(order))

def part_one():
   G = _adjacency_list()
   G['out'] = [] #add the adjacencies for 'out' - not in dataset
   topo_order = _topological_sort(G)
   
   ways = {} #number of simple paths from 'you' to a given node
   for node in topo_order:
       if node == 'you':
           for neig in G[node]:
               ways[neig] = 1
       else:
           if node in ways:
               for neig in G[node]:
                   if neig not in ways:
                       ways[neig] = ways[node]
                   else :
                       ways[neig] = ways[neig] + ways[node]
   
   return ways['out']

def part_two():
    G = _adjacency_list()
    G['out'] = [] #add the adjacencies for 'out' - not in dataset
    topo_order = _topological_sort(G)
    
    def path_between(n1,n2):
        """Number of path between two nodes. CTRL-V from part one"""
        ways = {}
        for node in topo_order:
            if node == n1:
                for neig in G[node]:
                    ways[neig] = 1
            else:
                if node in ways:
                    for neig in G[node]:
                        if neig not in ways:
                            ways[neig] = ways[node]
                        else :
                            ways[neig] = ways[neig] + ways[node]
        return ways[n2]
    
    #find which of the DAC or the fast fourier transform comes first
    for node in topo_order:
        if node == 'dac':
            stops = ('dac', 'fft')
            break
        elif node == 'fft':
            stops = ('fft', 'dac')
            break
    
    return path_between('svr',stops[0])*path_between(stops[0], stops[1])*path_between(stops[1],'out')
        
       
            
    
    

if __name__ == "__main__":
    print(f"Answer: {part_two()}")
    