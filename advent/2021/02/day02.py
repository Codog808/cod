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

#day02("example").part1()
day02("input").part1()

                

