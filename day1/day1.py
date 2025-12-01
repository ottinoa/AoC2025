"""Day 1 in Advent of Code 2025
Find the password to enter the North Pole.
Input : sequence of rotations on a dial numbered 0-99.
    Clockwise rotations are written 'Rxx'
    Anticlockwise rotations are written 'Lxx'
The password is the number of time the pointer crosses 0.

1. Get the input from a text file.
2. Clean up the input, return a list of integers.
3. For each rotation in the sequence :
    3.1. Update the value on the dial
    3.2. Increment the value of the password when the pointer crossed 0.
"""

f = open("input.txt", 'r')
str_sequence = f.read()

#split the sequence into a list of rotations
str_sequence = str_sequence.splitlines()
#cleanup : integers instead of strings
int_sequence = []
for r in str_sequence:
    r = r.replace("R", "")
    r = r.replace("L", "-")
    int_sequence.append(int(r))

pointer = 50 #position of the dial
password = 0
for r in int_sequence:
    if pointer == 0 and r < 0:
        #Prevent double-counting of L turns when the dial starts at 0
        password -=1
    pointer += r
    while pointer <0:
        pointer +=100
        password +=1
    while pointer >=100:
        pointer -=100
        if pointer !=0:
            #Prevent double-counting of R turns when the dial ends on 0
            password +=1
    if pointer == 0:
        password +=1

print("The password is " + str(password))