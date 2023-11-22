import ctools
def main():
    raw = ctools.wopen("day4.d")
    work_order = raw.strip().split("\n")
    oelf = ''
    telf = ''
    total = 0
    for p, pair in enumerate(work_order):
        # oelf, telf = pair.strip().split(",")
        elves = pair.strip().split(",")
        for x, elf in enumerate(elves):
            origin, to = elf.strip().split("-")
            #print(f"this is origin {origin}\nthis is to{to}")
            if x == 0:
                oelf = (int(origin), int(to))
            elif x == 1:
                telf = (int(origin), int(to))
        if oelf[0] <= telf[0] <= oelf[1] and oelf[0] <= telf[1] <= oelf[1]:
            #print(p,"l", oelf, telf)
            total += 1
        elif telf[0] <= oelf[0] <= telf[1] and telf[0] <= oelf[1] <= telf[1]:
            #print(p, "r",oelf, telf)
            total += 1
        #else:
            #print(p, "w", oelf, telf)
        oelf = ''
        telf = ''
    #answer to part 1
    print(total)

    ### CHANGE THE TOTAL + STATEMENTS TO OR INSTEAD OF AND
    oelf = ''
    telf = ''
    total = 0
    for p, pair in enumerate(work_order):
        # oelf, telf = pair.strip().split(",")
        elves = pair.strip().split(",")
        for x, elf in enumerate(elves):
            origin, to = elf.strip().split("-")
            #print(f"this is origin {origin}\nthis is to{to}")
            if x == 0:
                oelf = (int(origin), int(to))
            elif x == 1:
                telf = (int(origin), int(to))
        if oelf[0] <= telf[0] <= oelf[1] or oelf[0] <= telf[1] <= oelf[1]:
            #print(p,"l", oelf, telf)
            total += 1
        elif telf[0] <= oelf[0] <= telf[1] or telf[0] <= oelf[1] <= telf[1]:
            #print(p, "r",oelf, telf)
            total += 1
        #else:
            #print(p, "w", oelf, telf)
        oelf = ''
        telf = ''
    # answer to part 2
    print(total)

if __name__ == "__main__":
    main()

