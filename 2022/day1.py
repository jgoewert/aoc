from aocd.models import Puzzle
from collections import Counter


def part1(input):
    elves = []
    calories = 0
    for line in input:
        if line.isnumeric():
            calories += int(line)
        else:
            # blank line
            elves.append(calories)
            calories = 0

    #add the last elf
    elves.append(calories)
    print ("Part 1: {}".format(max(elves)))

def part2(input):
    elves = []
    calories = 0
    for line in input:
        if line.isnumeric():
            calories += int(line)
        else:
            # blank line
            elves.append(calories)
            calories = 0
    #add the last elf
    elves.append(calories)
    elves.sort(reverse=True)
    print ("Part 2: {}".format(elves[0]+elves[1]+elves[2]))

if __name__ == "__main__":
    puzzle = Puzzle(year=2022, day=1)
 
    example = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""
    #part1(example.splitlines())
    #part1(puzzle.input_data.splitlines())
    part2(example.splitlines())
    part2(puzzle.input_data.splitlines())