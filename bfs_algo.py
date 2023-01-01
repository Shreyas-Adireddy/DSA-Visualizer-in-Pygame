from queue_ll import Queue


def bfs_search(grid, start):
    path = []
    start_x, start_y = start
    grid[start_x][start_y] = 2
    queue = Queue()
    queue.enqueue(item=(start_x, start_y))
    while not queue.is_empty():
        x, y = queue.dequeue()
        path.append((x, y))

        if grid[x][y] == 1:
            return path

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0]) and grid[x + dx][y + dy] != -2 and grid[x + dx][y + dy] != 2 and not (x + dx, y + dy) in path:
                if grid[x + dx][y + dy] == 1:
                    return path
                queue.enqueue((x + dx, y + dy))
                if grid[x + dx][y + dy] != 1:
                    grid[x + dx][y + dy] = 2

    return path

if __name__ == '__main__':
    grid = [[-1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, -1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
    start = (0, 0)
    end = (2, 2)

    path = bfs_search(grid, start)
    print(path)