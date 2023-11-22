def bfs_shortest_path(graph, start, end):
    # A queue to keep track of nodes to be processed
    queue = []
    visited = set(start)
    while queue:
        (current_node, path) = queue.pop(0)
        # Check all the neighbors of the current node
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                # If this is the end node, return the path
                if neighbor == end:
                    return path + [neighbor]
                queue.append((neighbor, path + [neighbor]))
        return None  # Path not found

def my_attempt(data):
    """ 
    'abadsfsdf',
    'asdfasdfd',
    'qwtqerwqe'
    is the format of the data.
    """
    start, end = (0,0), (0,0)
    for y, line in enumerate(data):
        for x, character in enumerate(line):
            if character == "S":
                start = (x, y)
                print(start)
            elif character == "E":
                end = (x,y)
                print(end)
            else:
                pass

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    neighbors = {
            "left": (-1, 0),
            "right": (1,0),
            "up": (0,-1),
            "down": (0, 1)
            }
    position = start
    elevation = "a"
    queue = [(start, elevation)]
    visited = set(start)
    while True:
        position, elevation = queue.pop(0)
        # check for corners
        check_neighbors = []
        for key in neighbors:
            x1, y1 = neighbors[key]
            x2, y2 = position
            dx = x2 + x1
            x, y = 0, 0
            if 0 <= dx < len(data[0]):
                x = dx
            dy = y2+y1
            if 0 <= dy < len(data) - 1:
                y = dy
            if y == 0 and x == 0:
                pass
            else:
                check_neighbors.append((x, y))

        # compare.
        check_neighbor_elevation = []
        for pos in check_neighbors:
            print(pos)
            neighbor = data[pos[1]][pos[0]]
            print(neighbor)
            if neighbor == "E":
                pass
            else:
                neighbor_elevation = alphabet.index(neighbor) + 1
                d_elevation = alphabet.index(elevation) + 1 - neighbor_elevation
                if -1 <= d_elevation <= 1:
                    check_neighbor_elevation.append((neighbor, pos))
        # find the shortest path...      
        for good_neighbor, good_position in check_neighbor_elevation:
            if good_position not in visited:
                visited.add(good_position)
                if good_neighbor == "z":
                    print(len(visited))
                    break
                queue.append((good_position, good_neighbor))
        print("CURRENT ELEVATION", elevation)
        if elevation == "z":
            break
    print("success")

from heapq import heappop ,heappush
def bastardized_main(data, start, end):
    """ copying William Y. Feng """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    grid = [list(line) for line in data]
    rows = len(grid)
    cols = len(grid[0])
    start, end = (0,0), (0,0)
    # print(grid)
    # for i in range(rows):
    #     for j in range(cols):
    #         print(i, j)
    #         char = grid[i][j]
    #         if char == "S":
    #             start = i, j
    #         if char == "E":
    #             end = i, j
    visited = [[False] * cols for _ in range(rows)]
    heap = [(0, start[0], start[1])]
    while True:
        steps, i, j = heappop(heap)

        if visited[i][j]:
            continue
        visited[i][j] = True

        if (i, j) == end:
            return steps
            break

        for ii, jj in neighbors(grid, i, j, rows, cols, alphabet):
            heappush(heap, (steps + 1, ii, jj))

def my_attempt_part2(data):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    grid = [list(line) for line in data]
    rows = len(grid)
    cols = len(grid[0])
    start, end = (0,0), (0,0)
    # print(grid)
    best_path = []
    starts = set()
    for i in range(rows):
        for j in range(cols):
            # print(i, j)
            char = grid[i][j]
            if char == "S":
                starts.add((i, j))
            if char == "a":
                starts.add((i, j))
            if char == "E":
                end = i, j
    for s in starts:
        steps = main(data, s, end)
        best_path.append(steps)
    print(best_path)
def height(char, key):
    if char in key:
        return key.index(char)
    if char == "S":
        return 0
    if char == "E":
        # One above the alphabet
        return 26
    return 0

def neighbors(grid, i, j, rows, cols, key):
    for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        ii = i + di
        jj = j + dj
        if not (0 <= ii < rows and 0 <= jj < cols):
            continue
        if height(grid[ii][jj], key) <= height(grid[i][j], key) + 1:
            yield ii, jj

from heapq import heappop ,heappush
def part1(data):
    """ copying William Y. Feng """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    grid = [list(line) for line in data]
    rows = len(grid)
    cols = len(grid[0])
    start, end = (0,0), (0,0)
    # print(grid)
    for i in range(rows):
        for j in range(cols):
            # print(i, j)
            char = grid[i][j]
            if char == "S":
                start = i, j
            if char == "E":
                end = i, j
    visited = [[False] * cols for _ in range(rows)]
    heap = [(0, start[0], start[1])]
    while True:
        steps, i, j = heappop(heap)
        if visited[i][j]:
            continue
        visited[i][j] = True
        if (i, j) == end:
            return steps
            break
        for ii, jj in neighbors(grid, i, j, rows, cols, alphabet):
            heappush(heap, (steps + 1, ii, jj))

def neighbors2(grid, i, j, rows, cols, key):
    for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        ii = i + di
        jj = j + dj
        if not (0 <= ii < rows and 0 <= jj < cols):
            continue
        if height(grid[ii][jj], key) >= height(grid[i][j], key) - 1:
            yield ii, jj

def part2(data):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    grid = [list(line) for line in data]
    rows = len(grid)
    cols = len(grid[0])
    start, end = (0,0), (0,0)
    # print(grid)
    for i in range(rows):
        for j in range(cols):
            # print(i, j)
            char = grid[i][j]
            if char == "S":
                start = i, j
            if char == "E":
                end = i, j
    visited = [[False] * cols for _ in range(rows)]
    # starting at the end
    heap = [(0, end[0], end[1])]
    while True:
        steps, i, j = heappop(heap)
        if visited[i][j]:
            continue
        visited[i][j] = True
        if height(grid[i][j], alphabet) == 0:
            return steps
        for ii, jj in neighbors2(grid, i, j, rows, cols, alphabet):
            heappush(heap, (steps + 1, ii, jj))




if __name__ == "__main__":
    with open("day12.d") as f:
        data = f.read().strip().split("\n")
    test = 'Sabqponm\nabcryxxl\naccszExk\nacctuvwj\nabdefghi'
    test = test.split("\n")
    # a is the lowest elevation, z is the highest elevation
    # (capital) S is User, (capital) E is destination.
    # can only move: up, down, left, right
    # can only go up an elevation of 1 or equal
    print(part1(data))
    print(part2(data))
    # part2(data)


        
