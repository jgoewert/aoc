from aocd.models import Puzzle
import numpy as np
from collections import defaultdict

def part1(input):
    cratesinput, instructioninput = input.split("\n\n")

    # parse the list by rows
    crates = np.array([list(crate) for crate in cratesinput.splitlines()])
    crates[(crates == " ") | (crates == "[") | (crates == "]")] = ""    
    columns = [value for value, column in enumerate(crates[-1]) if column != ""]

    # Rotate the columns
    crates = crates[:-1, columns].T
    crates_dict = defaultdict(list)
    for value, stack in enumerate(crates):
        crates_dict[value + 1] = list(reversed(list(stack[stack != ""])))

    #print(crates_dict)
    
    for instruction in instructioninput.splitlines():
        count, fromlocation, tolocation = list(map(int, (instruction.replace("move ", "").replace(" from ", ",").replace(" to ", ",").split(","))))
        #print (instructionvals)
        crates_dict[tolocation] += list(reversed(crates_dict[fromlocation][-count:]))
        crates_dict[fromlocation] = crates_dict[fromlocation][:-count]

    tops = "".join([topcrates[-1] for topcrates in crates_dict.values()])
    print ("Part 1: {}".format(tops))

def part2(input):
    cratesinput, instructioninput = input.split("\n\n")

    # parse the list by rows
    crates = np.array([list(crate) for crate in cratesinput.splitlines()])
    crates[(crates == " ") | (crates == "[") | (crates == "]")] = ""    
    columns = [value for value, column in enumerate(crates[-1]) if column != ""]

    # Rotate the columns
    crates = crates[:-1, columns].T
    crates_dict = defaultdict(list)
    for value, stack in enumerate(crates):
        crates_dict[value + 1] = list(reversed(list(stack[stack != ""])))

    #print(crates_dict)
    
    for instruction in instructioninput.splitlines():
        count, fromlocation, tolocation = list(map(int, (instruction.replace("move ", "").replace(" from ", ",").replace(" to ", ",").split(","))))
        #print (instructionvals)
        crates_dict[tolocation] += crates_dict[fromlocation][-count:]
        crates_dict[fromlocation] = crates_dict[fromlocation][:-count]

    tops = "".join([topcrates[-1] for topcrates in crates_dict.values()])
    print ("Part 2: {}".format(tops))

if __name__ == "__main__":
    puzzle = Puzzle(year=2022, day=5)
 
    example = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""
    

    
    #part1(example)
    part1(puzzle.input_data)
    #part2(example)
    part2(puzzle.input_data)