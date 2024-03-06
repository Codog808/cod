class day02:
    def __init__(self, filename):
        self.data = ((line.split()[0], int(line.split()[1])) for line in open(filename))

        self.h = 0
        self.d = 0
    def part1(self):
        for command in self.data:
            if command[0] == "forward":
                self.h += command[1]
            elif command[0] == "up":
                self.d -= command[1]
            else:
                self.d += command[1]

        print("answer for part 1\n" + str(self.h * self.d))

def data(filename):
    return ((line.split()[0], int(line.split()[1])) for line in open(filename))
def part2(filename):
    operations = data(filename)
    depth = 0
    horizontal_position = 0
    
    aim = 0
    for i, op in enumerate(operations):
        print(op)
        if op[0] == "forward":
            depth += aim * op[1]
            horizontal_position += op[1]
            print(i, aim, horizontal_position)
        elif op[0] == "up":
            aim -= op[1]
            print(i, aim, "up")
        elif op[0] == "down":
            aim += op[1]
            print(i, aim, "down")

    print("Horizontal Position: " + str(horizontal_position))
    print("Depth: " + str(depth))
    print("The answer to part 2: ")
    print(depth * horizontal_position)




#day02("example").part1()
day02("input").part1()

part2("input")
