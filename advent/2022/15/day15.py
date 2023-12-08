import re

def manhattan_dist(pair, com_pair):
    return abs(pair[0]-com_pair[0]) + abs(pair[1]- com_pair[1])

def part_1(filename, Y=2_000_000):
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

    # print(sensors)
    # print(beacons)
    distances = [manhattan_dist(sensor, beacon) for sensor, beacon in zip(sensors, beacons)]
    # print(distances)
    interval = []
    for i, sensor in enumerate(sensors):
        offset = distances[i] - abs(sensor[1] - Y)
        if offset <= 0:
            continue
        interval.append((sensor[0] - offset, sensor[0] + offset))

    # print(interval)
    taken_x = []
    for bx, by in beacons:
        if by == Y:
            taken_x.append(bx)

    # print(taken_x)
    min_of_the_intervals = min([i[0] for i in interval])
    max_of_the_intervals = max([i[1] for i in interval])

    ans = 0
    for x in range(min_of_the_intervals, max_of_the_intervals + 1):
        if x in taken_x:
            continue
        for left, right in interval:
            if left <= x <= right:
                ans += 1
                break
    print(ans)

def part_2(filename, Y=2_000_000):
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

    # print(sensors)
    # print(beacons)
    distances = [manhattan_dist(sensor, beacon) for sensor, beacon in zip(sensors, beacons)]
    # print(distances)
    # change of parsing here...
    pos = []
    neg = []
    for i, sensor in enumerate(sensors):
        d = distances[i]
        neg.extend([sensor[0] + sensor[1] - d, sensor[0] + sensor[1] + d])
        pos.extend([sensor[0] - sensor[1] - d, sensor[0] - sensor[1] + d])

    positive = None
    negative = None
    for i in range(2 * len(sensors)):
        for j in range(i + 1, 2 * len(sensors)):
            a, b = pos[i], pos[j]
            if abs(a-b)== 2:
                positive = min(a, b) + 1

            a, b = neg[i], neg[j]
            if abs(a-b) == 2:
                negative = min(a, b) + 1

    x, y = (positive + negative) // 2, (negative - positive) // 2
    ans = x * 4000000 + y
    print(ans)
    

    
part_1("input")
part_2("input")
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

