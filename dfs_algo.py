
def dfs_search(grid, start):
    path = []
    start_x, start_y = start
    grid[start_x][start_y] = 2
    stack = []
    stack.append((start_x, start_y))
    while len(stack):
        x, y = stack.pop()
        path.append((x, y))

        if grid[x][y] == 1:
            return path

        for dx, dy in [(0, 1), (-1, 0),(0, -1),  (1, 0)]:
            if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0]) and grid[x + dx][y + dy] != 2 and not (x + dx, y + dy) in path and grid[x + dx][y + dy] != -2:
                if grid[x + dx][y + dy] == 1:
                    return path
                stack.append((x + dx, y + dy))
                if grid[x + dx][y + dy] != 1:
                    grid[x + dx][y + dy] = 2

    return path



if __name__ == '__main__':
    grid = [[-1, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
    start = (0, 0)
    end = (2, 2)

    path = dfs_search(grid, start)
    print(path)