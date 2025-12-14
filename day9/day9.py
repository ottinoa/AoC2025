import numpy as np
from itertools import pairwise

INPUT_PATH = "inputs/example.txt"

def part_one(input_file):
    array = np.loadtxt(input_file, delimiter = ',', dtype = 'int')
    A = [] #list of areas
    
    #loop through each possible pair of vectors
    for i, vec1 in enumerate(array):
        for vec2 in array[i+1:]:
            A.append(np.prod(1+vec1-vec2))
    
    return max(A)

def _prepare_arrays(input_file):
    dataset = np.loadtxt(input_file, delimiter = ',', dtype = 'int')
    
    
    candidates = []
    borders = []
    
    #loop through each possible pair of vectors
    for i, vec1 in enumerate(dataset):
        for vec2 in dataset[i+1:]:
            area = np.prod(abs(1+vec1-vec2))
            candidates.append((area, vec1, vec2))
    
    for vec1, vec2 in pairwise(dataset):
        if vec1[0] == vec2[0]:
            #first dimension is the same => add a border
            borders.append((vec1[0], sorted([vec1[1],vec2[1]])))
                
    cand_dtype = np.dtype([
    ('area', np.int64),
    ('vec1', np.int32, (2,)),
    ('vec2', np.int32, (2,))])
    candidates_np = np.array(candidates, dtype=cand_dtype)
    
    bord_dtype = np.dtype([
    ('idx', np.int32),
    ('span', np.int32, (2,))])
    borders_np = np.array(borders, dtype=bord_dtype)

    return candidates_np, borders_np

def part_two(input_file):
    candidates, borders = _prepare_arrays(input_file)
    candidates[::-1].sort(order='area') #sort by descending area
    borders.sort(order='idx')
    
    for c in candidates:
        green1 = (c['vec1'][0], c['vec2'][1])
        green2 = (c['vec2'][0], c['vec1'][1])
        found = True
        for x,y in (green1, green2):
            border_count = 0 #number of times we cross the border
            for bor in borders:
                if bor['idx'] > x:
                    break #we walk from the edge to our green tile
                if y >= bor['span'][0] and y <= bor['span'][1]:
                    border_count +=1 #we cross a border
            print (c['area'], border_count, c['vec1'], c['vec2'])
            if border_count %2 == 0:
                #pairwise number of crossings => green tile ouside of country
                #break loop and try next candidate
                found = False
                break
        if found:
            return c['area']
    

if __name__ == "__main__":
    print(f"Answer : {part_two(INPUT_PATH)}")
            