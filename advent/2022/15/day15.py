import re

def part1(file):
    """
    Problem: None of the detected beacons seem to be producing a distress signal so you need to ... (refer to sovle)
    Solve: IN the row y=2000000, how many positions cannot contain a beacon?
    """
    pattern = re.compile(r"-?\d+")
    for line in open(file):
        sx, sy, bx, by = map(int, pattern.findall(line))
    print(sx, sy, bx, by)

part1("example")

