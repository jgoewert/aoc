from aocd.models import Puzzle
from collections import Counter

def part1(input):
    transitions = dict(Counter(input))
    floor = transitions["("] - transitions[")"]

    print ("Part 1: {}".format(floor))

def part2(input):
    counter = 0
    floor = 0
    for transition in input:
        counter = counter + 1
        match transition:
            case "(":
                floor = floor + 1
            case ")":
                floor = floor - 1
        if floor < 0:
            break

    print ("Part 2: {}".format(counter))

if __name__ == "__main__":
    puzzle = Puzzle(year=2015, day=1)
 
    example = ")())())"
    #part1(example)
    part1(puzzle.input_data)
    example2 = "()())"
    #part2(example2)
    part2(puzzle.input_data)