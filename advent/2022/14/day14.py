def simulate_sand(filled, sand_source, max_y):
    x, y = sand_source
    while y <= max_y:
        if (x, y+1) not in filled:
            y += 1
            coninue
        if (x - 1, y + 1) not in filled:
            x -= 1
            y += 1
            continue

        if (x - 1, y + 1) not in filled:
            x += 1
            y += 1

        filled.add((x,y))

def part1():
    with open("day14.d") as f:
        map_pieces = f.read().strip().split()
    sand_source = 500, 0
    filled = set()
    for piece in map_pieces:
        coords = []
        for str_coords in line.split(" -> "):
            x, y = map(int, str_coord.split(","))
            coords.append((x, y))
            
        for i in range(1, len(coords)):
            # iterate all besides one to cleanly compare every item to the one before
            cx, cy = coords[i]
            px, py = coords[i-1]

            if cy != py:
                assert cx == px
                # send an assert error if it is wrong
                for y in range(min(cx, px), max(cx, px) + 1):
                    # get the min and the max between the two value then add 1 to the max in order to get more 
                    filled.add(cx, y)
                    # form the up and down of the map

            if cx != px:
                assert cy == py
                for x in range(min(cx, px), max(cx, px) + 1):
                    filled.add(x, cy)
    
    max_y = max(coord[1] for coord in filled)
    # find the deepest the cave goes by iterating through the set


