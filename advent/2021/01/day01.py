"""
https://github.com/nitekat1124/advent-of-code-2021/blob/main/solutions/day01.py
"""

class day01:
    def __init__(self, data):
        self.input = [int(line) for line in open(data)]

    def nitekat_part1(self):
        c = sum(1 for i in range(1, len(self.input)) if self.input[i] > self.input[i-1])
        print(c)
    def part1(self):
        init = self.input[0]
        inc = 0
        dec = 0 
        print(str(init) + " inital")
        for line in self.input[1:]:
            if init < line:
                inc += 1
                print(str(line) + " Increased")
            else:
                dec += 1
                print(str(line) + " Decreased")
            init = line

        print("\nAnswer for part 1")
        print(inc)
    def part2(self):
        inc = 0
        dec = 0
        init = [self.input[0], self.input[1], self.input[2]]
        for i in range(3, len(self.input)):
            a = sum([self.input[i-1], self.input[i-2], self.input[i-3]])
            b = sum([self.input[i], self.input[i-1], self.input[i-2]])
            if b > a:
                print(str(b) + " increased")
                inc += 1
            elif a > b:
                print(str(b) + " decrease")
            else:
                print(str(b) + " no change")

        print("Answer for part 2")
        print(str(inc))


#day01("example").part1()

#day01("input").part1()

#day01("input").nitekat_part1()

day01("example").part2()
day01("input").part2()
