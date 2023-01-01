import pygame
from cell import Cell
from constants import *
from dfs_algo import dfs_search
from bfs_algo import bfs_search
from a_star_algo import a_star_search


class Board:
    def __init__(self, screen, row, col):
        self.screen = screen
        self.row = row
        self.col = col
        self.grid = [[_ for _ in range(self.row)] for _ in range(self.col)]
        for i in range(row):
            for j in range(col):
                self.grid[i][j] = Cell(self.screen, i, j)
        self.colour = BLUEISH_COLOR

    def all_squares(self, instant, color):
        for i in range(self.row):
            for j in range(self.col):
                self.grid[i][j].draw(instant)
                self.grid[i][j].color = color
        pygame.display.update()

    def move(self, shift):
        for i in range(self.row):
            for j in range(self.col):
                self.grid[i][j].change_pos(*shift)
        self.all_squares(instant=True, color=self.colour)

    def zoom_in(self):
        if self.grid[0][0].side_len < 60:
            for row in self.grid:
                for cls in row:
                    cls.change_width(1)

    def zoom_out(self):
        if self.grid[0][0].side_len > 10:
            for row in self.grid:
                for cls in row:
                    cls.change_width(-1)

    def get_cell_len(self):
        return self.grid[0][0].side_len

    def collide_point(self, x, y):
        for i in range(self.row):
            for j in range(self.col):
                if self.grid[i][j].surface.collidepoint((x, y)): return [True, i, j]
        return [False, None, None]

    def reset_marks(self, chg=0):
        for i in range(self.row):
            for j in range(self.col):
                self.grid[i][j].mark_cell(0)

    def get_board(self):
        res = [[_ for _ in range(self.row)] for _ in range(self.col)]
        for i in range(self.row):
            for j in range(self.col):
                res[j][i] = self.grid[i][j].get_mark()
        return res
        # return [[cls.get_mark() for cls in row] for row in self.grid]

    def find_start(self):
        for i in range(self.row):
            for j in range(self.col):
                if self.grid[i][j].get_mark() == -1:
                    return [i, j]
        return None

    def find_end(self):
        for i in range(self.row):
            for j in range(self.col):
                if self.grid[i][j].get_mark() == 1:
                    return [i, j]
        return None

    def dfs_graphics(self):
        arr = self.get_board()
        start = self.find_start()
        end = self.find_end()
        if start and end:
            start = start[::-1]
            path = dfs_search(arr, start)
            del path[0]
            # print(path)
            path = path[::-1]
            return self.animate_algo(path, 10)

    def bfs_graphics(self):
        arr = self.get_board()
        start = self.find_start()
        end = self.find_end()
        if start and end:
            start = start[::-1]
            path = bfs_search(arr, start)
            del path[0]
            # print(path)
            path = path[::-1]
            return self.animate_algo(path, 2)

    def a_star_graphics(self):
        arr = self.get_board()
        start = self.find_start()
        end = self.find_end()
        if start and end:
            start = tuple(start[::-1])
            end = end[::-1]
            path = a_star_search(arr, start, end)
            del path[0]
            path.pop()
            # print(path)
            path = path[::-1]
            return self.animate_algo(path, 10)

    def animate_algo(self, path, speed=10):
        while path:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            i, j = path.pop()
            self.grid[j][i].mark_cell(2)
            self.all_squares(True, BLUEISH_COLOR)
            pygame.display.update()
            pygame.time.delay(speed)
        return


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(SIZE_OF_DISPLAY)
    screen.fill(WHITE)
    pygame.display.update()
    b = Board(screen, 8, 8)
    print(b.get_board())
    b.all_squares(instant=False)
    Dragging = False
    b.grid[0][0].mark = 2
    while True:
        b.all_squares(instant=True)
        screen.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 2: Dragging = True
            elif event.type == pygame.MOUSEMOTION:
                shift = pygame.mouse.get_rel()
                if Dragging: b.move(shift)
            elif event.type == pygame.MOUSEBUTTONUP: Dragging = False
