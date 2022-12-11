from aocd.models import Puzzle
import operator
from math import prod

class Monkey:
    def __init__(self, items, operation, operationvalue, divisible, truepath, falsepath, inspections):
        self.items = items
        self.operation = operation
        self.operationvalue = operationvalue
        self.divisible = divisible
        self.truepath = truepath
        self.falsepath = falsepath
        self.inspections = 0

    def test(self, item, worrylevel=3, mod_factor: int = 0):
        self.inspections += 1
        worry = item
        target = 0
        match self.operation:
            case "+":
                if self.operationvalue == "old":
                    worry = worry + worry
                else:
                    worry = worry + int(self.operationvalue)
            case "*":
                if self.operationvalue == "old":
                    worry = worry * worry
                else:
                    worry = worry * int(self.operationvalue)
        worry = worry // worrylevel
        if mod_factor:
                worry = worry % mod_factor
        if worry % self.divisible == 0:
            target = self.truepath
        else:
            target = self.falsepath
        return worry, target


def part1(input):
    monkeys = []
    items = []
    operation = ""
    operationvalue = ""
    divisible = 0
    truepath = 0
    falsepath = 0

    for line in input:
        if line.find("Monkey") >= 0:
            pass
        elif line.find("Starting items:") >= 0:
            items = list(map(int, line.split(":")[1].split(",")))
        elif line.find("Operation:") >= 0:
            operation = line.split(" ")[6]
            operationvalue = line.split(" ")[7]
        elif line.find("Test:") >= 0:
           divisible = int(line.split(" ")[5])
        elif line.find("If true:") >= 0:
            truepath = int(line.split(" ")[9])
        elif line.find("If false:") >= 0:
            falsepath = int(line.split(" ")[9])
        else:
            monkeys.append(Monkey(items, operation, operationvalue, divisible, truepath, falsepath, 0))

    #append last monkey
    monkeys.append(Monkey(items, operation, operationvalue, divisible, truepath, falsepath, 0 ))

    for loop in range(20):
        for monkey in monkeys:
            while len(monkey.items) > 0:
                item = monkey.items.pop()
                worry, target = monkey.test(item)
                monkeys[target].items.append(worry)

    monkeycount = 0
    for monkey in monkeys:
        print("Monkey {}:".format(monkeycount))
        print(' '.join([str(i) for i in monkey.items]))
        monkeycount += 1

    sorted_monkeys = sorted(monkeys, key=operator.attrgetter('inspections'))
    print ("Part 1: {}".format(sorted_monkeys[-1].inspections * sorted_monkeys[-2].inspections))

def part2(input):
    monkeys = []
    items = []
    operation = ""
    operationvalue = ""
    divisible = 0
    truepath = 0
    falsepath = 0

    for line in input:
        if line.find("Monkey") >= 0:
            pass
        elif line.find("Starting items:") >= 0:
            items = list(map(int, line.split(":")[1].split(",")))
        elif line.find("Operation:") >= 0:
            operation = line.split(" ")[6]
            operationvalue = line.split(" ")[7]
        elif line.find("Test:") >= 0:
           divisible = int(line.split(" ")[5])
        elif line.find("If true:") >= 0:
            truepath = int(line.split(" ")[9])
        elif line.find("If false:") >= 0:
            falsepath = int(line.split(" ")[9])
        else:
            monkeys.append(Monkey(items, operation, operationvalue, divisible, truepath, falsepath, 0))

    #append last monkey
    monkeys.append(Monkey(items, operation, operationvalue, divisible, truepath, falsepath, 0 ))

    mod_factor = prod([monkey.divisible for monkey in monkeys])

    for loop in range(10000):
        if loop & 100:
            print("*", end = "")
        for monkey in monkeys:
            while len(monkey.items) > 0:
                item = monkey.items.pop()
                worry, target = monkey.test(item, 1, mod_factor)
                monkeys[target].items.append(worry)

    print("!")
    monkeycount = 0
    for monkey in monkeys:
        print("Monkey {}:".format(monkeycount))
        print(' '.join([str(i) for i in monkey.items]))
        monkeycount += 1

    sorted_monkeys = sorted(monkeys, key=operator.attrgetter('inspections'))
    print ("Part 2: {}".format(sorted_monkeys[-1].inspections * sorted_monkeys[-2].inspections))

if __name__ == "__main__":
    puzzle = Puzzle(year=2022, day=11)
 
    example = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""
    #part1(example.splitlines())
    part1(puzzle.input_data.splitlines())
    #part2(example.splitlines())
    part2(puzzle.input_data.splitlines())