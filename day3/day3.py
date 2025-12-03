import numpy as np

INPUT_PATH = "inputs/input.txt"
BATTERIES_PER_ROW = 12

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

def part_two(input_file):
    """Get batteries for the North Pole elevator
    Generalization of the part one problem for N batteries per row
    """
    with open(input_file, 'r') as f:
        lines = f.read().splitlines()
    total_joltage = 0
    for line in lines:
        batteries = np.array([digit for digit in line], dtype ='int')
        indexes = battery_picker(batteries)
        joltage = sum(10**(BATTERIES_PER_ROW-1-i)*batteries[indexes[i]] 
                      for i in range(BATTERIES_PER_ROW))
        print(joltage)
        total_joltage += joltage
    return total_joltage
            
            

def battery_picker(array, btr_nbr = BATTERIES_PER_ROW):
    """Return a list of the indexes of the batteries to pick for max joltage
    1. Pick the first battery. In the case of 12 batteries to pick, it's the
        battery with the highest voltage that is no less than 12 position from
        the end of the line.
    2. Record the index
    3. Offset the slice of the iterable to the right - search for the second
        battery ON THE RIGHT of the first one in the array
    2. Pick the second battery and subsequent batteries (same constraints)
    """
    offset = 0 #start the slice at this index
    ignore_from = len(array)-(btr_nbr-1) #end the slice at this index
    indexes = []
    for n in range(btr_nbr):
        pick = np.argmax(array[offset:ignore_from])
        #note that the pick is relative to the slice
        indexes.append(pick+offset) #pick relative to the entire list
        offset = offset+pick+1 # +1 because the same battery cannot be picked again
        ignore_from +=1
    return indexes
        

print("Answer: " +str(part_two(INPUT_PATH)))