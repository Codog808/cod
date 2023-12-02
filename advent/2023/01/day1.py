import re

def part1(file):
    pattern = re.compile(r"-?\d+")
    sum = 0
    for line in open(file):
        line_value = "".join(map(str, pattern.findall(line)))
        # print(line_value[0] + line_value[-1])
        sum += int(line_value[0] + line_value[-1])
        # print(line_value)
    print(sum)
part1("input")
