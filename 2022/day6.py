from aocd.models import Puzzle

def findUniqueOffset(input, length):
    for offset in range(0,len(input)-length):
        if (len(set(input[offset:offset+length])) == length):
            return offset + length

def part1(input):
    print ("Part 1: {}".format(findUniqueOffset(input,4)))

def part2(input):
    print ("Part 2: {}".format(findUniqueOffset(input,14)))

if __name__ == "__main__":
    puzzle = Puzzle(year=2022, day=6)
 
    example = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
    #part1(example)
    part1(puzzle.input_data)
    #part2(example.splitlines())
    part2(puzzle.input_data)