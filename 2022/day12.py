from aocd.models import Puzzle
import numpy as np
import networkx as nx

def part1(input):
    heightmap = np.array([[*line.strip()] for line in input])

    startlocation = tuple(*np.argwhere(heightmap=='S'))
    heightmap[startlocation] = 'a'
    endlocation = tuple(*np.argwhere(heightmap=='E'));
    heightmap[endlocation] = 'z'

    grid = nx.grid_2d_graph(*heightmap.shape, create_using=nx.DiGraph)
    grid.remove_edges_from([(x,y) for x,y in grid.edges if ord(heightmap[y]) > ord(heightmap[x])+1])

    pathlist = nx.shortest_path_length(grid, target=endlocation)

    print("Part 1: {}".format(pathlist[startlocation]))

def part2(input):
    heightmap = np.array([[*line.strip()] for line in input])

    startlocation = tuple(*np.argwhere(heightmap=='S'))
    heightmap[startlocation] = 'a'
    endlocation = tuple(*np.argwhere(heightmap=='E'));
    heightmap[endlocation] = 'z'

    grid = nx.grid_2d_graph(*heightmap.shape, create_using=nx.DiGraph)
    grid.remove_edges_from([(x,y) for x,y in grid.edges if ord(heightmap[y]) > ord(heightmap[x])+1])

    pathlist = nx.shortest_path_length(grid, target=endlocation)

    print("Part 2: {}".format(min(pathlist[count] for count in pathlist if heightmap[count]=='a')))


if __name__ == "__main__":
    puzzle = Puzzle(year=2022, day=12)
 
    example = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""
    #part1(example.splitlines())
    part1(puzzle.input_data.splitlines())
    #part2(example.splitlines())
    part2(puzzle.input_data.splitlines())