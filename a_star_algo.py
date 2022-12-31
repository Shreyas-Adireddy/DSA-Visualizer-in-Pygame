from priority_queue import PriorityQueue


def heuristic(a, b):
    x1, y1 = a
    x2, y2 = b
    return abs(x1 - x2) + abs(y1 - y2)


def a_star_search(grid, start, goal):
    path = []
    pq = PriorityQueue()
    pq.put(start, 0)
    g_values = {start: 0}
    while not pq.is_empty():
        x, y = pq.get()
        path.append((x,y))
        if grid[x][y] == 1:
            return path
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1),(1,1), (1,-1), (-1,1), (-1,-1)]:
            neighbour = (x + dx, y+dy)
            if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0]) and grid[x + dx][y + dy] != 2 and not (x + dx,
                                                                                                             y + dy) in path and neighbour not in g_values and grid[x + dx][y + dy] != -2:
                new_cost = g_values[(x,y)] + 1
                g_values[neighbour] = new_cost
                f_value = new_cost + heuristic(goal, neighbour)
                pq.put(neighbour, f_value)
    return None

if __name__ == '__main__':
    grid = [[-1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
    start = (0, 0)
    end = (2, 2)

    path = a_star_search(grid, start, end)
    print(path)