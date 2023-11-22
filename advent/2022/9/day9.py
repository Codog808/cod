import ctools
def touching(x1, y1, x2, y2):
    return abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1


def move(hx, hy, tx, ty, dx, dy):

    hx += dx
    hy += dy

    if not touching(hx, hy, tx, ty):
        sign_x = 0 if hx == tx else (hx - tx) / abs(hx - tx)
        sign_y = 0 if hy == ty else (hy - ty) / abs(hy - ty)

        tx += sign_x
        ty += sign_y

    return hx, hy, tx, ty
def move2(knots, dx, dy):
    
    knots[0][0] += dx
    knots[0][1] += dy

    for i in range(1, 10):
        hx, hy = knots[i - 1]
        tx, ty = knots[i]

        if not touching(hx, hy, tx, ty):
            sign_x = 0 if hx == tx else (hx - tx) / abs(hx - tx)
            sign_y = 0 if hy == ty else (hy - ty) / abs(hy - ty)

            tx += sign_x
            ty += sign_y

        knots[i] = [tx, ty]
    return knots

def main():
    """
    https://github.com/womogenes/AoC-2022-Solutions/blob/main/day_09/day_09_p2.py
    beyond my capabilities, therefore I must find outside sources...
    """
    # with open("day9.d") as fin:
    #     lines = fin.read().strip().split("\n")
    lines = ctools.wopen("day9.d").strip().splitlines()

    hx, hy = 0, 0
    tx, ty = 0, 0


    

    dd = {
        "R": [1, 0],
        "U": [0, 1],
        "L": [-1, 0],
        "D": [0, -1]
    }

    tail_visited = set()
    tail_visited.add((tx, ty))

    for line in lines:
        op, amount = line.split(" ")
        amount = int(amount)
        dx, dy = dd[op]

        for _ in range(amount):
            hx, hy, tx, ty = move(hx, hy, tx, ty, dx, dy)
            tail_visited.add((tx, ty))
    print("answer for part 1")
    print(len(tail_visited))
    
    knots = [[0,0] for _ in range(10)]

    tail_visited = set()
    tail_visited.add(tuple(knots[-1]))

    for line in lines:
        op, amount = line.split(" ")
        amount = int(amount)
        dx, dy = dd[op]

        for _ in range(amount):
            knots = move2(knots, dx, dy)
            tail_visited.add(tuple(knots[-1]))

    print("answer for part 2")
    print(len(tail_visited))


        
if __name__ == "__main__":
    # will_main()
    main()
    # main2()
        
# def main():
#     data = ctools.wopen("day9.d").strip().split("\n")
#     instructions = [tuple(i.strip().split(" ")) for i in data]
#     head = 0, 0
#     tail = []
#     for instruction in instructions:
#         d = int(instruction[1])
#         x, y = 0, 0
#         if instruction[0] == "L" or instruction[0] == "R":
#             if instruction[0] == "L":
#                 x = -1
#             elif instruction[0] == "R":
#                 x = 1
#             dx = d * x
#             for i in range(1, d+1):
#                 i = (i * x) + head[0]
#                 tail.append((i, head[1]))
#             head = (dx + head[0]), head[1]
#         else:
#             if instruction[1] == "U":
#                 y = -1
#             elif instruction[1] == "D":
#                 y = 1
#             dy = d * y
#             for i in range(1, d+1):
#                 i = (i*y) + head[1]
#                 tail.append((head[0], i))
#             head = head[0], (dy + head[1])

#         #     head = head[0], int(instruction[1])
#         # else:
#         #     head = int(instruction[1]), head[1]

#     length_tail = len(set(tail))
#     print(length_tail)
#     # print(instructions)
#     print("success")
# def main2():
#     instructions = [("R", 4), ("U", 4), ("L", 3), ("D", 1), ("R", 4), ("D", 1), ("L", 5), ("R", 2)]  # for demonstration
#     head = [0, 0]
#     tail = [0, 0]
#     visited = set()

#     dirs = {'R': [1, 0], 'L': [-1, 0], 'U': [0, 1], 'D': [0, -1]}

#     for direction, distance in instructions:
#         for _ in range(distance):
#             dx, dy = dirs[direction]
#             head[0] += dx
#             head[1] += dy

#             visited.add(tuple(tail))

#             # logic to move the tail
#             if abs(head[0] - tail[0]) >= 2:
#                 tail[0] += dx
#             if abs(head[1] - tail[1]) >= 2:
#                 tail[1] += dy

#     print(len(visited))

# head_x, head_y = 0,0
# tail_x, tail_y = 0,0
# def absolute_value(n):
#     if n < 0:
#         return n * -1
#     else:
#         return n

# def touching():
#     return (absolute_value(head_x - tail_x) <= 1 and
#             absolute_value(head_y - tail_y) <= 1)

# def move(dx, dy):
#     global head_x, head_y, tail_x, tail_y
#     head_x += dx
#     head_y += dy

#     if not touching():
#         sign_x = 0 if head_x == tail_x else (head_x - tail_x) / absolute_value(head_x - tail_x)
#         sign_y = 0 if head_y == tail_y else (head_y - tail_y) / absolute_value(head_y - tail_y)

#         tail_x += sign_x
#         tail_x += sign_y


# def will_main():
#     global head_x, head_y, tail_x, tail_y
#     # head and tail rope bridge simulator thing
#     head_movements = ctools.wopen("day9.d").strip().splitlines()
#     direction = {
#             "R":[1,0],
#             "L":[-1,0],
#             "U":[0,-1],
#             "D":[0,1],
#             }
#     tail_visited = set()
#     tail_visited.add((tail_x, tail_y))
#     for instruction in head_movements:
#         op, amount = instruction.split(" ")
#         amount = int(amount)
#         dx, dy = direction[op]

#         for _ in range(amount):
#             move(dx, dy)
#             tail_visited.add((tail_x, tail_y))

#     print(len(tail_visited))

