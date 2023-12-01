def is_int(x):
    try:
        int(x)
        return True
    except:
        return False

def prnt(x):
    print("\n\n", x, "\n\n")

def absolute_value(x):
    if x < 0:
        return x * -1
    else:
        return x

def main():
    prnt("Parsing the data...")
    with open("day9.d") as f:
        instructions = [i for i in f.read().strip().splitlines()]
        instruct = []
        for line in instructions:
            x = line.split(" ")
            y = (x[0], int(x[1]))
            instruct.append(y)
    instructions = instruct
    
    head_x, head_y = 0,0
    tail_x, tail_y = 0,0
    prnt("Following the instructions...")
    for op, d in instructions:
        if op == "R":
            head_x += d
        elif op == "L":
            head_x -= d
        elif op == "U":
            head_y -= d
        elif op == "D":
            head_y += d
        while True:
            if not absolute_value(tail_x - head_x) <= 1 and not absolute_value(tail_y - head_y) <= 1:
                # it is not adjacent, therefore make it...
                pass
            


            
        # print(head_x, head_y)
    # print(instructions)

if __name__ == "__main__":
    main()
