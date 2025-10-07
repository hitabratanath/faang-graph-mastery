from collections import deque

def minimumKnightMoves(x, y):
    x, y = abs(x), abs(y)
    queue = deque([(0, 0, 0)])
    visited = set([(0, 0)])
    directions = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [-1, 2], [1, -2], [-1, -2]]

    while queue:
        a, b, dist = queue.popleft()

        if (a, b) == (x, y): return dist

        for da, db in directions:
            na, nb = da + a, db + b
            if (na, nb) not in visited and na >= -2 and nb >= -2:
                visited.add((na, nb))
                queue.append((na, nb, dist + 1))

