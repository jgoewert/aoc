from aocd.models import Puzzle

def check_vector(values):
    #check increasing
    returnvalue = True
    for x in (range(len(values) - 1)):
        if values[x] < values[x+1]:
            returnvalue = False
            break
    if returnvalue == True:
        return True
    #check decreasing
    returnvalue = True
    for x in (range(len(values) - 1)):
        if values[x] > values[x+1]:
            returnvalue = False
            break
    if returnvalue == True:
        return True
    return False

def check_offsets(values):
    for x in (range(len(values)- 1)):
        if ((abs(int(values[x]) - int(values[x+1]))) >= 4):
            return False
        if ((int(values[x]) - int(values[x+1])) == 0):
            return False
    return True

def part1(input):
    sum = 0
    for stringvalue in input:
        stringarray = stringvalue.split()
        valuearray = [int(numeric_string) for numeric_string in stringarray]
        #print ("{} - {} - {}".format(stringvalue, check_vector(valuearray), check_offsets(valuearray)))
        if check_vector(valuearray) and check_offsets(valuearray):
            sum += 1

    print ("Part 1: {}".format(sum))

def part2(input):
    sum = 0
    for stringvalue in input:
        stringarray = stringvalue.split()
        valuearray = [int(numeric_string) for numeric_string in stringarray]
        #print ("{} - {} - {}".format(stringvalue, check_vector(valuearray), check_offsets(valuearray)))
        if check_vector(valuearray) and check_offsets(valuearray):
            sum += 1
        else:
            for removevalueindex in range(len(valuearray)):
                tempvaluearray = valuearray.copy()
                del tempvaluearray[removevalueindex] 
                if check_vector(tempvaluearray) and check_offsets(tempvaluearray):
                    sum += 1
                    break
        
    print ("Part 2: {}".format(sum))

if __name__ == "__main__":
    puzzle = Puzzle(year=2024, day=2)
    example = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""
    #part1(example.splitlines())
    part1(puzzle.input_data.splitlines())
    #part2(example.splitlines())
    part2(puzzle.input_data.splitlines())