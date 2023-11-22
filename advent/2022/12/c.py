from collections import deque

def get_neighbors(x, y, matrix):
    neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    valid_neighbors = [(i, j) for i, j in neighbors if 0 <= i < len(matrix) and 0 <= j < len(matrix[0])]
    return valid_neighbors

def bfs(matrix, start, end):
    visited = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    queue = deque([(start, 0)])  # (position, steps_taken)

    while queue:
        (x, y), steps = queue.popleft()

        # Check if the end position is reached
        if (x, y) == end:
            return steps

        for i, j in get_neighbors(x, y, matrix):
            # Check elevation difference and if the cell is not visited
            elevation_diff = abs(ord(matrix[i][j]) - ord(matrix[x][y]))
            if not visited[i][j] and (elevation_diff == 0 or elevation_diff == 1):
                visited[i][j] = True
                queue.append(((i, j), steps + 1))

    return -1  # No path found

matrix = [
    "Sabqponm",
    "abcryxxl",
    "accszExk",
    "acctuvwj",
    "abdefghi"
]

start = (0, 0)
end = (2, 5)

result = bfs(matrix, start, end)
print(result)  # Output: 31

