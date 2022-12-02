from aocd.models import Puzzle

scoredict = {
    "A X": 1+3, # RR
    "B X": 1+0, # PR
    "C X": 1+6, # SR
    "A Y": 2+6, # RP
    "B Y": 2+3, # PP
    "C Y": 2+0, # SP
    "A Z": 3+0, # RS
    "B Z": 3+6, # PS
    "C Z": 3+3  # SS
}

scoredict2 = {
    "A X": 3+0, # RR lose
    "B X": 1+0, # PR
    "C X": 2+0, # SR
    "A Y": 1+3, # RP
    "B Y": 2+3, # PP
    "C Y": 3+3, # SP
    "A Z": 2+6, # RS
    "B Z": 3+6, # PS
    "C Z": 1+6  # SS
}

def part1(input):
    global scoredict
    score = 0
    for line in input:
        score += scoredict[line]
    print ("Part 1: {}".format(score))

def part2(input):
    global scoredict2
    score = 0
    for line in input:
        score += scoredict2[line]
    print ("Part 2: {}".format(score))

if __name__ == "__main__":
    puzzle = Puzzle(year=2022, day=2)
 
    example = """A Y
B X
C Z"""

    #part1(example.splitlines())
    part1(puzzle.input_data.splitlines())
    #part2(example.splitlines())
    part2(puzzle.input_data.splitlines())