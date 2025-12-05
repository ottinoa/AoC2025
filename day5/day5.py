import re
INPUT_PATH = "inputs/input.txt"

def _cleanup_database(filepath):
    with open(filepath, 'r') as f:
        input_str = f.read()
    ranges = re.findall(r"(\d+)-(\d+)", input_str)
    numbers = input_str.split('\n\n')[1].splitlines()
    return ranges, numbers

def part_one(input_file):
    fresh_ranges, fruits = _cleanup_database(input_file)
    
    fresh_count = 0
    for fruit in fruits:
        for start, end in fresh_ranges:
            if int(fruit) >= int(start) and int(fruit) <= int(end):
                fresh_count+=1
                break #no double-counting fruits in multiple ranges
    
    return fresh_count

def part_two(input_file):
    data, fruits = _cleanup_database(input_file)
        #We don't need the fruits.
    
    stop_count = 0
    while stop_count < len(data):
        new_data = []
        append_yourself = True
        
        so, eo = map(int, data[0])
        for rnge in data[1:]:
            s, e = map(int, rnge)
            if so>=s and eo<=e:
                #range0 included in range : append range, do not append range0
                append_yourself = False
                new_data.append(rnge)
            elif so<s and eo>e:
                #range fully included : append nothing
                continue
            elif so<=e and eo>=s:
                #the ranges intersect, append a new range that includes both
                new_data.append((min(so,s), max(eo,e)))
                append_yourself = False
            else:
                #ranges outside of each other : append range
                new_data.append(rnge)
        
        if append_yourself:
            new_data.append(data[0])
            stop_count += 1
        else:
            stop_count = 0 #reset counter if modifications where made
        data = new_data
        print(len(data), stop_count)
        
    #calculate the output
    total_fresh = sum(int(e)-int(s)+1 for s,e in data)
    return total_fresh
            
    
if __name__ == "__main__":
    print("Answer: " + str(part_two(INPUT_PATH)))