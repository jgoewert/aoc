from aocd.models import Puzzle

def is_overlapping(coord):
    return max(coord[0][0],coord[1][0]) <= min(coord[0][1],coord[1][1])

def part1(input):
    coords = []
    count = 0
    for line in input:
        pairs = line.split(",")
        coords.append([list(map(int, pairs[0].split("-"))), list(map(int, pairs[1].split("-")))])
    for coord in coords:
        matched = False
        if (coord[0][0] <= coord[1][0]):
            if (coord[0][1] >= coord[1][1]):
                count += 1
                matched = True
        if (not matched):
            if (coord[1][0] <= coord[0][0]):
                if (coord[1][1] >= coord[0][1]):
                    count += 1
    print ("Part 1: {}".format(count))

def part2(input):
    coords = []
    count = 0
    for line in input:
        pairs = line.split(",")
        coords.append([list(map(int, pairs[0].split("-"))), list(map(int, pairs[1].split("-")))])
    for coord in coords:
        if is_overlapping(coord):
            count += 1
    print ("Part 1: {}".format(count))

if __name__ == "__main__":
    puzzle = Puzzle(year=2022, day=4)
 
    example = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""
    part1(example.splitlines())
    part1(puzzle.input_data.splitlines())
    part2(example.splitlines())
    part2(puzzle.input_data.splitlines())