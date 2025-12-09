import numpy as np
from itertools import groupby
import math

INPUT_PATH = "inputs/input.txt"
INPUT_ROWS = 4 #3 rows in example, 4 rows in input

def part_one(input_file, n = INPUT_ROWS):
    numbers = np.loadtxt(input_file, dtype = 'int', max_rows = n).transpose()
    operations = np.loadtxt(input_file, dtype = 'U', skiprows = n)
    grand_total = 0
    for idx, val in enumerate(numbers):
        if operations[idx] == '*':
            grand_total += val.prod()
        else:
            grand_total += val.sum()
    return grand_total

def part_two(input_file, n = INPUT_ROWS):
    operations = np.loadtxt(input_file, dtype = 'U', skiprows = n)
    with open(input_file, mode='r') as f:
        lines = f.read().splitlines()
    numbers = np.array([*map(list, lines[:-1])], dtype = 'U').transpose()
    #concatenate the numbers as strings
    human_str = [''.join(i).strip() for i in numbers]
    numbers = []
    #group the numbers to be operated on together 
    for blank, g in groupby(human_str, lambda x: x == ''):
        if not blank:
            numbers.append(list(g))
    
    #CTRL-V from part one
    grand_total = 0
    for idx, val in enumerate(numbers):
        if operations[idx] == '*':
            grand_total += math.prod(map(int, val))
        else:
            grand_total += sum(map(int, val))
    return grand_total

if __name__ == "__main__":
    print("Answer: " + str(part_two(INPUT_PATH)))