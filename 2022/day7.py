from aocd.models import Puzzle
from collections import defaultdict

def parseTree(input):
    tree = []
    directories = defaultdict(int)
    for line in input:
        match line.split():
            case ["$", "ls"]:
                pass
            case ["dir", directory]:
                pass
            case [filesize, filename]:
                directories[tuple(tree)] += int(filesize)
                path = tree[:-1]
                while path:
                    directories[tuple(path)] += int(filesize)
                    path.pop()
            case ['$', 'cd', '..']:
                tree.pop()
            case ['$', 'cd', path]:
                tree.append(path)
    return directories


    return directories
def part1(input):
    directories = parseTree(input)
    print ("Part 1: {}".format(sum([directory for directory in directories.values() if directory <= 100000])))

def part2(input):
    directories = parseTree(input)
    free = 70000000 - directories[('/',)]
    print ("Part 2: {}".format(min([directory for directory in directories.values() if directory + free >= 30000000])))


if __name__ == "__main__":
    puzzle = Puzzle(year=2022, day=7)

    example = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""
    #part1(example.splitlines())
    part1(puzzle.input_data.splitlines())
    #part2(example.splitlines())
    part2(puzzle.input_data.splitlines())
