from aocd.models import Puzzle
import numpy as np

class GridPoint:
    obstacle: bool = False
    visited: bool = False
    def __init__(self, obstacle):
        self.obstacle = obstacle
        self.visited = False

def func(a):
    return a.visited

def printmap(gridmap):
    for y in range(gridmap.shape[1]):
        for x in range(gridmap.shape[0]):
            if gridmap[x,y].visited:
                print("X", end="")
            elif gridmap[x,y].obstacle:
                print("#", end="")
            else:
                print(".", end="")
        print("")
    print("")
    print("")

def part1(input):
    gridmap = np.ndarray(shape=(len(input),len(input[0])), dtype=GridPoint)
    position = [0,0]
    direction = 1 #up
    #print (gridmap.dtype)
    for y in range(len(input)):
        for x in range(len(input[y])):
            if input[y][x] == "^":
                position[0] = x
                position[1] = y
            if input[y][x] == "#":
                gridmap[x,y] = GridPoint(True)
            else:
                gridmap[x,y] = GridPoint(False)

    while True:
        gridmap[position[0],position[1]].visited = True
        #printmap(gridmap)
        match direction:
            case 1:
                if position[1] == 0:
                    break #Walked off the side
                if gridmap[position[0], position[1]-1].obstacle:
                    direction += 1
                else:
                    position[1] -= 1
            case 2: 
                if position[0] == len(input[0])-1:
                    break #Walked off the side
                if gridmap[position[0]+1, position[1]].obstacle:
                    direction += 1
                else:
                    position[0] += 1
            case 3: 
                if position[1] == len(input)-1:
                    break #Walked off the side
                if gridmap[position[0], position[1]+1].obstacle:
                    direction += 1
                else:
                    position[1] += 1
            case 4: 
                if position[0] == 0:
                    break #Walked off the side
                if gridmap[position[0]-1, position[1]].obstacle:
                    direction = 1
                else:
                    position[0] -= 1
    printmap(gridmap)         
    total = 0

    for y in range(gridmap.shape[1]):
        for x in range(gridmap.shape[0]):
            if gridmap[x,y].visited:
                total += 1
    
    print ("Part 1: {}".format(total))

def part2(input):
    originalgridmap = np.ndarray(shape=(len(input),len(input[0])), dtype=GridPoint)
    position = [0,0]
    direction = 1 #up
    #print (gridmap.dtype)
    for y in range(len(input)):
        for x in range(len(input[y])):
            if input[y][x] == "^":
                position[0] = x
                position[1] = y
            if input[y][x] == "#":
                originalgridmap[x,y] = GridPoint(True)
            else:
                originalgridmap[x,y] = GridPoint(False)

    while True:
        originalgridmap[position[0],position[1]].visited = True
        #printmap(gridmap)
        match direction:
            case 1:
                if position[1] == 0:
                    break #Walked off the side
                if originalgridmap[position[0], position[1]-1].obstacle:
                    direction += 1
                else:
                    position[1] -= 1
            case 2: 
                if position[0] == len(input[0])-1:
                    break #Walked off the side
                if originalgridmap[position[0]+1, position[1]].obstacle:
                    direction += 1
                else:
                    position[0] += 1
            case 3: 
                if position[1] == len(input)-1:
                    break #Walked off the side
                if originalgridmap[position[0], position[1]+1].obstacle:
                    direction += 1
                else:
                    position[1] += 1
            case 4: 
                if position[0] == 0:
                    break #Walked off the side
                if originalgridmap[position[0]-1, position[1]].obstacle:
                    direction = 1
                else:
                    position[0] -= 1
    printmap(originalgridmap) 
    total = 0
    #For each visited spot, test the location
    for y in range(len(input)):
        for x in range(len(input[0])):
            print("Row {} of {}, Column {} of {}".format(y, len(input), x, len(input[0])))
            if originalgridmap[x,y].visited != True:
                continue #only do visited spots
            gridmap = np.ndarray(shape=(len(input),len(input[0])), dtype=GridPoint)
            loopmax = gridmap.shape[0] * gridmap.shape[1]
            position = [0,0]
            direction = 1 #up
            #print (gridmap.dtype)
            for ay in range(len(input)):
                for ax in range(len(input[y])):
                    if input[ay][ax] == "^":
                        position[0] = ax
                        position[1] = ay
                    if input[ay][ax] == "#":
                        gridmap[ax,ay] = GridPoint(True)
                    else:
                        gridmap[ax,ay] = GridPoint(False)

            if (x == position[0]) and (y == position[1]):
                continue #skip start point
            if gridmap[x,y].obstacle:
                continue
            else:
                gridmap[x,y].obstacle = True
            #printmap(gridmap)
            
            maxcount = gridmap.shape[1] * gridmap.shape[0]
            while True:
                maxcount -= 1
                if (maxcount <= 0):
                    total += 1
                    break

                gridmap[position[0],position[1]].visited = True
                #printmap(gridmap)
                match direction:
                    case 1:
                        if position[1] == 0:
                            break #Walked off the side
                        if gridmap[position[0], position[1]-1].obstacle:
                            direction += 1
                        else:
                            position[1] -= 1
                    case 2: 
                        if position[0] == len(input[0])-1:
                            break #Walked off the side
                        if gridmap[position[0]+1, position[1]].obstacle:
                            direction += 1
                        else:
                            position[0] += 1
                    case 3: 
                        if position[1] == len(input)-1:
                            break #Walked off the side
                        if gridmap[position[0], position[1]+1].obstacle:
                            direction += 1
                        else:
                            position[1] += 1
                    case 4: 
                        if position[0] == 0:
                            break #Walked off the side
                        if gridmap[position[0]-1, position[1]].obstacle:
                            direction = 1
                        else:
                            position[0] -= 1
            #printmap(gridmap) 
    

                
    print ("Part 2: {}".format(total))

if __name__ == "__main__":
    puzzle = Puzzle(year=2024, day=6)
 
    example = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""
    #part1(example.splitlines())
    #part1(puzzle.input_data.splitlines())
    #part2(example.splitlines())
    part2(puzzle.input_data.splitlines())