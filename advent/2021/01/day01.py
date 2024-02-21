

class day01:
    def __init__(self, data):
        self.input = [int(line) for line in open(data)]

    def part1(self):
        init = self.input.pop(0)
        inc = 0
        dec = 0 
        print(init + " inital")
        for line in self.input:
            if init < line:
                inc += 1
                print(line + " Increased")
            else:
                dec += 1
                print(line + " Decreased")
            init = line

        print("\nAnswer for part 1")
        print(inc)
            

day01("example").part1()

day01("input").part1()
