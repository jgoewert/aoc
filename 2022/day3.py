from aocd.models import Puzzle
import string

def get_priority(character: str) -> int:
    return string.ascii_letters.index(character) + 1


def part1(input):
    total = 0
    for items in input:
        midpoint = len(items)//2
        matches = set(items[:midpoint]).intersection(
            items[midpoint:]
        )
        for match in matches:
            total += string.ascii_letters.index(match) + 1
    print ("Part 1: {}".format(total))

def part2(input):
    total = 0
    for elf in range(0,len(input),3):
        matches = set(input[elf]).intersection(input[elf+1], input[elf+2])
        for match in matches:
            total += string.ascii_letters.index(match) + 1

    print ("Part 2: {}".format(total))

if __name__ == "__main__":
    puzzle = Puzzle(year=2022, day=3)
 
    example = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""
    #part1(example.splitlines())
    part1(puzzle.input_data.splitlines())
    #part2(example.splitlines())
    part2(puzzle.input_data.splitlines())