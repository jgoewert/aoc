from aocd.models import Puzzle

def moveKnot(parent, knot):
    if (abs(parent[0]-knot[0]) >= 2) or (abs(parent[1]-knot[1]) >= 2):
        if (parent[0] < knot[0]):
            knot[0] -= 1
        elif (parent[0] > knot[0]):
            knot[0] += 1
        if (parent[1] < knot[1]):
            knot[1] -= 1
        elif (parent[1] > knot[1]):
            knot[1] += 1
    return knot
    
def part1(input):
    head = [0,0]
    tail = [0,0]
    visited = []
    for step in input:
        direction, distance = step.split(" ")
        for count in range(int(distance)):
            match (direction):
                case "U":
                    head[1] += 1
                case "D":
                    head[1] -= 1
                case "L":
                    head[0] -= 1
                case "R":
                    head[0] += 1
            tail = moveKnot(head, tail)
            visited.append([])
            visited[len(visited)-1] = tuple(tail.copy())
            #print ("{} - {}".format(head,tail))
    steps = set(visited)
    print ("Part 1: {}".format(len(steps)))

def part2(input):
    knots=[[0,0] for i in range(10)]
    visited = []
    for step in input:
        direction, distance = step.split(" ")
        for count in range(int(distance)):
            match (direction):
                case "U":
                    knots[0][1] += 1
                case "D":
                    knots[0][1] -= 1
                case "L":
                    knots[0][0] -= 1
                case "R":
                    knots[0][0] += 1
            for count in range(1,10):
                knots[count] = moveKnot(knots[count-1], knots[count])
            visited.append([])
            visited[len(visited)-1] = tuple(knots[len(knots)-1].copy())
            #print ("{} - {}".format(head,tail))
    steps = set(visited)
    print ("Part 2: {}".format(len(steps)))

if __name__ == "__main__":
    puzzle = Puzzle(year=2022, day=9)
 
    example = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

    example2 = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""
    #part1(example.splitlines())
    part1(puzzle.input_data.splitlines())
    #part2(example.splitlines())
    #part2(example2.splitlines())
    part2(puzzle.input_data.splitlines())