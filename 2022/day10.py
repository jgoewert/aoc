from aocd.models import Puzzle



def part1(input):
    registerx = 1
    cycle = 0
    cycleruntime = 0
    instructioncount = -1
    currentinstruction  = ["","0"]
    sum = 0

    while instructioncount < len(input)-1:
        cycleruntime -= 1
        if cycleruntime <= 0:
            #process instruction
            match currentinstruction[0]:
                case "addx":
                    registerx += int(currentinstruction[1])
                #case "noop":

            instructioncount += 1

            currentinstruction = input[instructioncount].split()
            match currentinstruction[0]:
                case "addx":
                    cycleruntime = 2
                case "noop":
                    cycleruntime = 1
        cycle += 1
        match cycle:
            case 20 | 60 | 100 | 140 | 180 | 220:
                sum += registerx * cycle
                print("Cycle {} {}".format(cycle, registerx * cycle))

    
    print ("Part 1: {}".format(sum))

def part2(input):
    picture = ["","","","","",""]
    registerx = 1
    cycle = 0
    cycleruntime = 0
    instructioncount = -1
    currentinstruction  = ["","0"]
    sum = 0
    outline = []
    cyclestep = 0
    while instructioncount < len(input)-1:
        cycleruntime -= 1
        if cycleruntime <= 0:
            #process instruction
            match currentinstruction[0]:
                case "addx":
                    registerx += int(currentinstruction[1])
                #case "noop":

            instructioncount += 1

            currentinstruction = input[instructioncount].split()
            match currentinstruction[0]:
                case "addx":
                    cycleruntime = 2
                case "noop":
                    cycleruntime = 1

        if (registerx == cyclestep) or (registerx-1 == cyclestep)  or (registerx+1 == cyclestep):
            outline.append("#")
        else:
            outline.append(".")
        cycle += 1
        cyclestep += 1
        match cycle:
            case 40 | 80 | 120 | 160 | 200 | 240:
                print("".join(outline))
                outline = []
                sum += registerx * cycle
                cyclestep = 0
                #print("Cycle {} {}".format(cycle, registerx * cycle))
    print ("Part 2: {}".format(0))

if __name__ == "__main__":
    puzzle = Puzzle(year=2022, day=10)
    
    example = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""
    #part1(example.splitlines())
    part1(puzzle.input_data.splitlines())
    #part2(example.splitlines())
    part2(puzzle.input_data.splitlines())