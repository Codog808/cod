"""
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

references:
    - https://www.youtube.com/watch?v=bLMj50cpOug&list=PLnNm9syGLD3yf-YW-a5XNh1CJN07xr0Kz&index=16
        a video explaining how to solve the problem. 
"""
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

    print("Answer to part 1: ")

def p2(filename):
    for line in open(filename):
        print(line)

    print("Answer to part 2: ")

p1("example")
# p2("example")
