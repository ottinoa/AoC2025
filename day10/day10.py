import numpy as np
from itertools import combinations, combinations_with_replacement
import re

INPUT_PATH = "inputs/input.txt"

def _create_dataset_p1(path=INPUT_PATH):
    goals = []
    buttons = []
    with open(path, 'r') as f:
        lines = f.read().splitlines()
    for line in lines:
        goal_str = re.search(r"\[([#\.]*)\]", line).group(1)
        goal = []
        for c in goal_str:
            if c == '#':
                goal.append(True)
            if c == '.':
                goal.append(False)
        goal = np.array(goal, dtype='?')
        goals.append(goal)
        
        buttons_str = re.findall(r"\(([,\d]*)\)", line)
        button = np.full((len(buttons_str), len(goal)), False, dtype='?')
        for i, button_str in enumerate(buttons_str):
            for idx in map(int, button_str.split(',')):
                button[i,idx] = True
        buttons.append(button)
        
    return goals, buttons

def xor(start, array):
    left = start
    for line in array:
        left = np.bitwise_xor(left, line)
    return left

def part_one():
    """Naive implementation testing all the possible button combinations
    Time complexity =(2^N) where N is the number of buttons.
    """
    goals, buts = _create_dataset_p1()
    print(goals)
    button_presses = []
    for i in range(len(goals)):
        goal = goals[i]
        buttons = buts[i]
        comb_not_found = True
        press_count = 1
        while comb_not_found:
            button_comb = combinations(buttons, press_count)
            for comb in button_comb:
                if np.sum(xor(goal, comb)) == 0:
                    #by combining the goal and the buttons, all lights should go off
                    comb_not_found = False
                    button_presses.append(press_count)
                    break
            press_count +=1
    return sum(button_presses)

def _create_dataset_p2(path=INPUT_PATH):
    joltages = []
    buttons = []
    with open(path, 'r') as f:
        lines = f.read().splitlines()
    for line in lines:
        jolt_str = re.search(r"\{([\d,]*)\}", line).group(1)
        joltage = []
        for n in jolt_str.split(','):
            joltage.append(n)
        joltage = np.array(joltage, dtype = 'i')
        joltages.append(joltage)
        
        buttons_str = re.findall(r"\(([,\d]*)\)", line)
        button = np.zeros((len(buttons_str), len(joltage)), dtype= 'i')
        for i, button_str in enumerate(buttons_str):
            for idx in map(int, button_str.split(',')):
                button[i,idx] = 1
        buttons.append(button)
    return joltages, buttons

def part_two():
    """Bruteforce solution testing all button combinations (with replacement)
    """
    joltages, buts = _create_dataset_p2()
    button_presses = []
    print(f"{len(joltages)} lines to test")
    for i in range (len(joltages)):
        jolt = joltages[i]
        buttons = buts[i]
        comb_not_found = True
        press_count = 1
        
        while comb_not_found:
            print(f"Line {i} testing {press_count} button presses")
            button_comb = combinations_with_replacement(buttons, press_count)
            for comb in button_comb:
                comb = np.array(comb)
                if np.array_equal(np.sum(comb, axis=0), jolt):
                    comb_not_found = False
                    button_presses.append(press_count)
                    break
            press_count +=1
    return sum(button_presses)
        


print(f"Answer: {part_two()}")