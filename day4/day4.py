"""Advent of Code 2025
Day 4 : Printing Department
"""
import numpy as np

INPUT_PATH = "inputs/input.txt"
NEIGHBOUR_VECTORS = [(-1,-1),(-1,0),(-1,1),(0,-1),
                     (0,1),(1,-1),(1,0),(1,1)]
    #position of possible neighbours relative to the paper roll

def part_one(input_file):
    """Return the number of paper rolls that are forklift accessible.
    The rolls are mapped on a 2D grid (input from text file).
    A roll is accessible if it as AT MOST 3 neighbours on the grid
        out of 8 possible (up, down, left, right and diagnonal).
    """
    #Translate the input file into an int8 matrix (roll ==1, no roll ==0)
    grid = []
    with open(input_file, 'r') as f:
        lines = f.read().splitlines()
    for line in lines:
        grid_row = []
        for c in line:
            if c == '@':
                grid_row.append(1)
            elif c == '.':
                grid_row.append(0)
        grid.append(grid_row)
    grid = np.array(grid, dtype='int8')
    
    #For each neighbour of a roll, increment its value by one
    max_y, max_x = grid.shape
    for idx, val in np.ndenumerate(grid):
        if val == 0: continue #ignore positions with no rolls
        xo, yo = idx
        for x,y in NEIGHBOUR_VECTORS:
            if xo+x>=0 and yo+y>=0 and xo+x <max_x and yo+y<max_y: #in the grid
                if grid[xo+x, yo+y] !=0:
                    val +=1
        grid[idx] = val #write the new value in the array
    
    return len(grid[(grid > 0) & (grid <=4)])


def part_two(input_file):
    """Same problem but recursive: remove rolls until it's not possible, count
    the removed rolls
    """
    #Translate the input file into an int8 matrix (roll ==1, no roll ==0)
    grid = []
    with open(input_file, 'r') as f:
        lines = f.read().splitlines()
    for line in lines:
        grid_row = []
        for c in line:
            if c == '@':
                grid_row.append(1)
            elif c == '.':
                grid_row.append(0)
        grid.append(grid_row)
    grid = np.array(grid, dtype='int8')
    max_y, max_x = grid.shape
    
    rolls_removed = 0

    while True:
        #For each neighbour of a roll, increment its value by one
        for idx, val in np.ndenumerate(grid):
            if val == 0: continue #ignore positions with no rolls
            xo, yo = idx
            for x,y in NEIGHBOUR_VECTORS:
                if xo+x>=0 and yo+y>=0 and xo+x <max_x and yo+y<max_y: #in the grid
                    if grid[xo+x, yo+y] !=0:
                        val +=1
            grid[idx] = val #write the new value in the array
        
        to_remove = len(grid[(grid > 0) & (grid <=4)])
        if to_remove > 0:
            did_something = True #new iteration if some rolls were removed
            rolls_removed += to_remove
            np.place(grid, (grid > 0) & (grid <=4), 0)
                #replace removed rolls by 0 in the grid
            np.place(grid, grid>4, 1)
                #reset non-removed rolls to 1 in the grid
        
        if did_something == False: #no changes this iteration
            break
        did_something = False
    
    return rolls_removed
    
if __name__ == "__main__":
    print("Answer: " + str(part_two(INPUT_PATH)))