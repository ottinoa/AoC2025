import numpy as np

INPUT_PATH = "inputs/input.txt"

def part_one(input_file):
    """Get batteries for the North Pole elevator
    From a text file containing rows of digits of the same length,
    Each digit representating the joltage of a single battery
    Create a numpy array
    Find the biggest combination of batteries from each row and sum them.
    1. Find the biggest battery of each row that is NOT the last one
        That's the tens (t)
    2. Find the biggest battery on the right of t in the row
        That's the units (u)
    3. Return sum(10t + u) for all ranks
    """
    with open(input_file, 'r') as f:
        raw_input = f.read()
    total_joltage = 0
    lines = raw_input.splitlines()
    for line in lines:
        batteries = np.array([digit for digit in line], dtype ='int')
        #find the index of t (maximum v
        t_idx = np.argmax(batteries[:len(batteries)-1])
        #find the index of u relative to t then convert
        u_idx_rel = np.argmax(batteries[t_idx+1:])
        u_idx = t_idx + u_idx_rel + 1
        #calculate the joltage and sum
        local_joltage = 10*batteries[t_idx] + batteries[u_idx]
        total_joltage += local_joltage
        print(local_joltage)
        print(batteries)
    return total_joltage
    
print("Answer: " +str(part_one(INPUT_PATH)))