from aocd.models import Puzzle

def part1(input):
    list1 = []
    list2 = []    
    for pairs in input:
        splitpair = pairs.split()
        list1.append(int(splitpair[0]))
        list2.append(int(splitpair[1]))
    list1.sort()
    list2.sort()

    sum = 0
    for x in range(len(list1)):
        #print ("{} - {} = {}".format(list1[x], list2[x],abs(list1[x] - list2[x])))
        sum += abs(list1[x] - list2[x])

    print ("Part 1: {}".format(sum))

def part2(input):
    list1 = []
    list2 = []    
    for pairs in input:
        splitpair = pairs.split()
        list1.append(int(splitpair[0]))
        list2.append(int(splitpair[1]))
    
    sum = 0
    for x in range(len(list1)):
        #print ("{}  = {}".format(list1[x], list2.count(list1[x])))
        sum += (list1[x] * list2.count(list1[x]))

    print ("Part 2: {}".format(sum))

if __name__ == "__main__":
    puzzle = Puzzle(year=2024, day=1)
 
    example = """3   4
4   3
2   5
1   3
3   9
3   3"""
    #part1(example.splitlines())
    #part1(puzzle.input_data.splitlines())
    part2(example.splitlines())
    part2(puzzle.input_data.splitlines())