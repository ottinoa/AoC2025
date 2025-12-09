import numpy as np
from functools import lru_cache

INPUT_PATH = "inputs/input.txt"

def part_one(input_file):
    with open(input_file, mode='r') as f:
        diagram = f.read().splitlines()
    lasers = [0 for i in range(len(diagram[0]))]
    split_count = 0
    for line in diagram[:-1]:
        for idx, c in enumerate(line):
            if c == 'S':
                #start beam
                lasers[idx] = 1
                break
            if lasers[idx] == 1 and c == '^':
                #if you can split the beam
                split_count +=1
                lasers[idx] = 0
                if idx-1 >= 0:
                    lasers[idx-1] = 1
                if idx+1 < len(lasers):
                    lasers[idx+1] = 1
    return split_count

def part_two(input_file):
    with open(input_file, mode='r') as f:
        lines = f.read().splitlines()
        splitters = []
        for line in lines[::2]:
            splitter_idx = set()
            for idx, char in enumerate(line):
                if char == 'S':
                    col_orig = idx #initial position of the beam
                    break
                elif char == '^':
                    splitter_idx.add(idx)
            if len(splitter_idx) > 0:
                splitters.append(splitter_idx)
        
        #optimization - compute the tree (stored as a dict)
        nextrow = {}
        for r in range(len(splitters)):
            for col in splitters[r]:
                left_target = None
                right_target = None
                
                for next_r in range(r+1, len(splitters)):
                    #for each splitter, find the row of next splitter on the l and r
                    if col-1 in splitters[next_r] and left_target is None:
                        left_target = next_r
                    if col+1 in splitters[next_r] and right_target is None:
                        right_target = next_r
                    if left_target and right_target:
                        break
                nextrow[(r,col)] = (left_target, right_target)
        
        @lru_cache(None)
        def rec_split(r, col):
            """the recursive function"""
            next_left, next_right = nextrow[(r, col)]
            timecount = 1 #each splitter creates a timeline

            if next_left is not None:
                #go left
                timecount += rec_split(next_left, col-1)
            if next_right is not None:
                #go right
                timecount += rec_split(next_right, col+1)
            
            #if not at the end of the timeline, pass the timelines along
            return timecount
            
        return rec_split(0, col_orig) + 1 #1 = the original timeline
                  
def _rec_splitter(splitters, row, col, timecount = 1):
    """DEPRECIATED -- Too slow, new one with lru_cache"""
    print(timecount)
    timecount +=1 #a new timeline is created every time the beam splits
    for r, c in enumerate(splitters[row+1:], start=row+1):
        if col-1 in c:
            timecount = _rec_splitter(splitters, r, col-1, timecount)
            break
    for r, c in enumerate(splitters[row+1:], start=row+1):
        if col+1 in c:
            timecount = _rec_splitter(splitters, r, col+1, timecount)
            break
    return timecount

            
        

if __name__ == "__main__":
    print("Answer: " + str(part_two(INPUT_PATH)))