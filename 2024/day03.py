from aocd.models import Puzzle
import re

def part1(input):
    cleanedinput = re.findall(r"mul\(\d{1,3},\d{1,3}\)",input)
    #print(cleanedinput)
    sum = 0
    for function in cleanedinput:
        values = re.search(r"\d{1,3},\d{1,3}", function).group(0).split(",")
        sum += int(values[0]) * int(values[1])
        #print(values)
    print ("Part 1: {}".format(sum))

def part2(input):
    cleanedinput = re.findall(r"(mul\(\d{1,3},\d{1,3}\)|don\'t\(\)|do\(\))",input)
    #print(cleanedinput)
    sum = 0
    enabled = True
    for function in cleanedinput:
        if (function.find("don't()") > -1):
            enabled = False
        elif (function.find("do()")  > -1):
            enabled = True
        else:
            if enabled:
                values = re.search(r"\d{1,3},\d{1,3}", function).group(0).split(",")
                #print(values)
                sum += int(values[0]) * int(values[1])
    print ("Part 2: {}".format(sum))

if __name__ == "__main__":
    puzzle = Puzzle(year=2024, day=3)
 
    example = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    example2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    #part1(example)
    part1(puzzle.input_data)
    #part2(example2)
    part2(puzzle.input_data)