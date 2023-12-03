import re

def manhattan_dist(pair, com_pair):
    return abs(pair[0]-com_pair[0]) + abs(pair[1]- com_pair[1])

def part_1(filename, Y=2000000):
    """
    https://github.com/womogenes/AoC-2022-Solutions/blob/main/day_15/day_15_p1.py

    https://www.youtube.com/watch?v=w7m48_uCvWI&t=47s
    """
    pattern = re.compile(r"-?\d+")
    sensors, beacons = [], []
    for line in open(filename):
        sx, sy, bx, by = map(int, pattern.findall(line))
        sensors.append((sx, sy))
        beacons.append((bx, by))
    distances = [manhattan_dist(sensor, beacon) for sensor, beacon in zip(sensors, beacons)]
    
part_1("example")

#import re

#def slow(file):
#    """
#    Problem: None of the detected beacons seem to be producing a distress signal so you need to ... (refer to sovle)
#    Solve: IN the row y=2000000, how many positions cannot contain a beacon?
#    """
#    pattern = re.compile(r"-?\d+")
#    cannot = set()
#    known = set()

#    Y = 2000000

#    # another way to loop through each line of the file, feels more vertexical.
#    for line in open(file):
#        sx, sy, bx, by = map(int, pattern.findall(line))
#        # find the absolute distance. 
#        d = abs(sx -bx) + abs(sy -by)
#        # all (x, y): abs(sx - x) + abs(sy = y) <= d    y = Y = 10
#        offset = d - abs(sy - Y)

#        if offset < 0:
#            continue
#        #boundary
#        lx = sx - offset
#        hx = sx + offset
#        for x in range(lx, hx + 1):
#            cannot.add(x)
#        if by == Y:
#            known.add(bx)

#    print(len(cannot - known))

#def fast_part1(file):
#    """
#    Problem: None of the detected beacons seem to be producing a distress signal so you need to ... (refer to sovle)
#    Solve: IN the row y=2000000, how many positions cannot contain a beacon?
#    """
#    pattern = re.compile(r"-?\d+")
#    Y = 2000000
    
#    intervals = []
#    # another way to loop through each line of the file, feels more vertexical.
#    for line in open(file):
#        sx, sy, bx, by = map(int, pattern.findall(line))
#        # find the absolute distance. 
#        d = abs(sx -bx) + abs(sy -by)
#        # all (x, y): abs(sx - x) + abs(sy = y) <= d    y = Y = 10
#        offset = d - abs(sy - Y)

#        if offset < 0:
#            continue
#        lx = sx - offset
#        hx = sx + offset

#        intervals.append((lx, hx))
#    #sorted by lower to upper
#    intervals.sort()
#    q = []
#    for lo, hi in intervals:
#        if not q:
#            q.append((lo, hi))
#            continue
#        qlo, qhi = q[-1]
#        if lo > qhi + 1:
#            q.append([lo, hi])
#            continue
#        qhi = max((qhi, hi))
#    print(q)

# slow("input")

