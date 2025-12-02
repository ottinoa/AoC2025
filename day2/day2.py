import re
from math import log10

INPUT_PATH = "inputs/input.txt"

def part_one(input_file):
    """Return the sum of the wrong IDs in the North Pole gift shop
    1. From a text file, create a list of possible wrong IDs (as ints)
    2. Check if the first half of the ID matches the second half (e.g. 123123)
    3. If it does, it's wrong: add it to the sum
    """
    with open(input_file, 'r') as f:
        raw_input = f.read()
    sum = 0
    #iterate on the possible wrong IDs using regex
    id_range_pattern = re.compile(r"(\d+)-(\d+)")
    id_range_list = id_range_pattern.findall(raw_input)
    for id_range in id_range_list:
        start, end = id_range
        for i in range(int(start),int(end)+1):
            #compare first and second half of the string
            s = str(i)
            h = len(s)//2
            if s[:h] == s[h:]:
                sum += i
    return sum

def part_two(input_file):
    """Return the sum of the wrong IDs in the North Pole gift shop
        1. From a text file, create a list of possible wrong IDs (as ints)
        2. Check the ID for repeating sequences (e.g. 123123, 242424)
        3. If it is made of repeating sequences, it's wrong: add it to the sum
        """
    with open(input_file, 'r') as f:
        raw_input = f.read()
    sum = 0
    #iterate on the possible wrong IDs using regex
    id_range_pattern = re.compile(r"(\d+)-(\d+)")
    id_range_list = id_range_pattern.findall(raw_input)
    for id_range in id_range_list:
        start, end = id_range
        for id in range(int(start),int(end)+1):
            
            #Start of iteration on the IDs
            sid = str(id)
            length = len(sid)
            #Test repetition for each denominator of len(sid)
            #the id.
            for part in range(1, length//2+1): #max length = n/2 digits
                if length % part !=0: #optional
                    continue
                #split the id into substrings of equal length
                substrings = [sid[i:i+part] for i in range(0, length - part + 1, part)]
                #check if all substrings are identical (size of set = 1)
                if len(set(substrings)) == 1:
                    print(sid)
                    sum += id
                    break #Prevent double-counting (e.g. 22-22-22, 222-222)
                
            
    return sum
                

print("Answer: " + str(part_two(INPUT_PATH)))