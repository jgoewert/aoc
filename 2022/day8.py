from aocd.models import Puzzle
from math import prod

class Forest:
    def __init__(self, trees):
        self.trees = trees
        self.rowsize = (0, len(trees)-1)
        self.columnsize = (0, len(trees[0])-1)

    def checkVisible(self,x,y):
        return any((self.trees[y][x] == max(subset) and subset.count(self.trees[y][x]) == 1) for subset in self.subsetrow(x, y)+self.subsetcolumn(x, y))

    def subsetrow(self, x, y):
        return [self.trees[y][:x+1], self.trees[y][x:]]

    def subsetcolumn(self, x, y):
        return ["".join([self.trees[line][x] for line in range(0, y+1)]), "".join([self.trees[line][x] for line in range(y, self.rowsize[1]+1)])]

    def totalVisible(self, reduce_fn, process_fn):
        return reduce_fn(process_fn(x, y) for x in range(self.rowsize[1] + 1) for y in range(self.columnsize[1] + 1))

    def findSurroundVisible(self, x, y):
        rslices, cslices = self.subsetrow(x, y), self.subsetcolumn(x, y)
        return prod([visibleCheck(self.trees[y][x], slice) for slice in [rslices[0][::-1], rslices[1], cslices[0][::-1], cslices[1]]])

def visibleCheck(height, row):
    for i in range(1, len(row)-1):
        if row[i] >= height:
            return i
    return len(row)-1

#class Tree:
#    def __init__(self, height, visible):
#        self.height = height
#        self.visible = visible

def printTrees(trees):
    for y in range(0,len(trees)):
        for x in range(0,len(trees[0])):
            print("{}".format(trees[y][x].height), end = '')
        print("")
    for y in range(0,len(trees)):
        for x in range(0,len(trees[0])):
            if (trees[y][x].visible):
                print("*", end = '')
            else:
                print(".", end = '')

        print("")

def part1(input):
    forest = Forest(input)
    # for line in input:
    #     treeline = []
    #     for char in line:
    #         treeline.append(Tree(int(char), False))
    #     trees.append(treeline)

    # #Top Row / Bottom Row
    # for x in range(0,len(trees[0])):
    #     trees[0][x].visible = True
    #     trees[len(trees)-1][x].visible = True

    # #Left Column / Right Column
    # for y in range(0,len(trees)):
    #     trees[y][0].visible = True
    #     trees[y][len(trees[0])-1].visible = True

    # for y in range(1,len(trees)):
    #      for x in range(1,len(trees[0])):
    #         if (max(trees[y][0:x].height) < trees[y][x]):
    #             trees[y][x].visible = True

    # # By Row
    # for y in range(1,len(trees)):
    #     #Left to Right
    #     for x in range(1,len(trees[0])):
    #         if trees[y][x].height >= trees[y][x-1].height:
    #             trees[y][x].visible = True
    #         else:
    #             break
    # for y in range(1,len(trees)):
    #     #Right to Left
    #     for x in range(-2,-len(trees[0]),-1):
    #         if trees[y][x].height >= trees[y][x+1].height:
    #             trees[y][x].visible = True
    #         else:
    #             break


    # #By Column Top to Bottom
    # for x in range(1,len(trees[0])):
    #     for y in range(1,len(trees)):
    #         if trees[y][x].height >= trees[y-1][x].height:
    #             trees[y][x].visible = True
    #         else:
    #             break
    # for x in range(1,len(trees[0])):
    #     #Bottom to Top
    #     for y in range(-2,-len(trees), -1):
    #         if trees[y][x].height >= trees[y+1][x].height:
    #             trees[y][x].visible = True
    #         else:
    #             break
    # printTrees(trees)

    # count = 0
    # for y in range(0,len(trees)):
    #     for x in range(0,len(trees[0])):
    #         if trees[y][x].visible == True:
    #             count += 1

    print ("Part 1: {}".format(forest.totalVisible(sum, forest.checkVisible)))

def part2(input):
    forest = Forest(input)
    print ("Part 2: {}".format(forest.totalVisible(max, forest.findSurroundVisible)))

if __name__ == "__main__":
    puzzle = Puzzle(year=2022, day=8)
 
    example = """30373
25512
65332
33549
35390"""

    #part1(example.splitlines())
    part1(puzzle.input_data.splitlines())
    #part2(example.splitlines())
    part2(puzzle.input_data.splitlines())