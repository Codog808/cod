import ctools
import sys

def check(X, cycle):
    print("within check...")
    checkpoints = [20,60,100,140,180,220]
    for i in checkpoints:
        print(i, cycle)
        if cycle == i:
            print(X * cycle)
            return X * cycle 
    # if no check points
    ctools.prnt("out of check...")
    return 0

def update_screen(G, X, cycle):
    # grabs the row by floor division
    row = (cycle-1) // 40
    # mod gives the remainder which is 0-39, or the proper indexes of G
    col = (cycle-1) % 40
    G[row][col] = ('#' if abs(X - (cycle-1)%40) <= 1 else " ")
    return G

def main():
    """ design a replacement video system """
    # 1. Signal set to the CPU
    ## single register, starts at 1, because of noop
    ## two instructions; addx V: increase x by V;noop: no effect
    ### addx +2 tick; noop +1 tick
    # 2. 
    data = ctools.wopen("day10.d")
    # to test against the example data.
    try:
        if sys.argv[1]:
            data = ctools.wopen(sys.argv[1])
    except:
        pass
    instructions = data.strip().split("\n")
    cycle = 0
    X = 1
    value = 0
    sum = 0
    for op in instructions:
        # cycle += 1
        # print(X, cycle)
        if not op == "noop":
            _, value = op.split(" ")
            value = int(value)
            cycle += 1
            # print(check(X, cycle))
            sum += check(X, cycle)
            cycle += 1
            sum += check(X, cycle)
            X += value
        else:
            cycle += 1
            print(check(X, cycle))
            sum += check(X, cycle)

    print("answer for part 1 is...")
    print(sum)
    ###########################################################3
    cycle = 0
    X = 1
    value = 0
    sum = 0
    G = [["?" for _ in range(40)] for _ in range(6)]
    for op in instructions:
        # cycle += 1
        # print(X, cycle)
        if not op == "noop":
            _, value = op.split(" ")
            value = int(value)
            cycle += 1
            # print(check(X, cycle))
            sum += check(X, cycle)
            update_screen(G, X, cycle)
            cycle += 1
            sum += check(X, cycle)
            update_screen(G, X, cycle)
            X += value
        else:
            cycle += 1
            print(check(X, cycle))
            sum += check(X, cycle)
            update_screen(G, X, cycle)

    print("answer for part 2 is...")
    for r in range(6):
        print("".join(G[r]))


    # print(clock, X)

    print("success")
if __name__ == "__main__":
    main()
        
