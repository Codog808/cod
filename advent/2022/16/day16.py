"""
Credit and References:
- https://www.youtube.com/watch?v=bLMj50cpOug&list=PLnNm9syGLD3yf-YW-a5XNh1CJN07xr0Kz&index=16
    a video explaining how to solve the problem. 
- https://github.com/womogenes/AoC-2021-Solutions/blob/main/day_16/day_16_p1.py
        
Elephants have a hand-held device that sends a distress beacon.

We need to get the elephants out of the cave
- first we must release the pressure of the volacano
- there is 30 minutes to escape

You can open a system of tunnels with valves that opens pipes
- it takes a minute to open the valves and another minute to move to a new valve
- All valves are closed
- You and the elephants start at valve AA
- the minutes-left * flow-rate = pressure_release

Find out how to release as much pressure as possible.


"""
from collections import deque

def dfs (time, valve, bitmask, cache, dists, indices, valves):
    if (time, valve, bitmask) in cache:
        return cache[(time, valve, bitmask)]

    maxval = 0
    for neighbor in dists[valve]:
        bit = 1 << indices[neighbor]
        if bitmask & bit:
            continue
        remtime = time - dists[valve][neighbor] - 1
        if remtime <= 0:
            continue
        maxval = max(maxval, dfs(remtime, neighbor, bitmask | bit, cache, dists, indices, valves)  + valves[neighbor] * remtime)
    cache[(time, valve, bitmask)] = maxval
    return maxval
      
def p1(filename):
    # dictionaries
    valves = {}
    tunnels = {}
    for line in open(filename):
        # print(line)
        line = line.strip()
        valve = line.split()[1]
        flow = int(line.split(";")[0].split("=")[1])
        targets = line.split("to ")[1].split(" ", 1)[1].split(", ")
        # print(line)
        # print(valve, flow, targets)
        valves[valve] = flow
        tunnels[valve] = targets

    dists = {}
    nonempty = []
    for valve in valves:
        if valve != "AA" and not valves[valve]:
            continue
        if valve != "AA":
            nonempty.append(valve)

        dists[valve] = {valve: 0, "AA": 0}
        visted = {valve}

        queue = deque([(0, valve)])
        # problem with queue.popleft() 12/12/23
        # Traceback (most recent call last):
        # File "C:\Users\shita\Projects\code\advent\2022\16\day16.py", line 95, in <module>
        #   p1("example")
        # File "C:\Users\shita\Projects\code\advent\2022\16\day16.py", line 67, in p1
        #   distance, position = queue.popleft()
        #   ^^^^^^^^^^^^^^^^^^
        while queue:
            distance, position = queue.popleft()
            for neighbor in tunnels[position]:
                if neighbor in visted:
                    continue
                visted.add(neighbor)
                if valves[neighbor]:
                    dists[valve][neighbor] = distance + 1
                queue.append((distance + 1, neighbor))

        del dists[valve][valve]
        if valve != "AA":
            del dists[valve]["AA"]

    indices = {}
    for index, element in enumerate(nonempty):
        indices[element] = index

    cache = {}

    print("Answer to part 1: ")
    print(dfs(30, "AA", 0, cache, dists, indices, valves))

def p2(filename):
    for line in open(filename):
        print(line)

    print("Answer to part 2: ")

# p1("example")
p1("input")
# p2("example")
# p2("input")
