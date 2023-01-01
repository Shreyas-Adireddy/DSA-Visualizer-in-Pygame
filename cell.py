from constants import *
import pygame

class Cell(pygame.sprite.Sprite):
    def __init__(self, screen, row, col, mark=0):
        self.screen = screen
        self.row = row
        self.col = col
        self.mark = mark
        self.side_len = CELL_WIDTH
        self.cordx = self.row * self.side_len + self.row
        self.cordy = self.col * self.side_len + self.col
        self.surface = None
        self.screen = screen
        self.color = BLUEISH_COLOR

    def draw(self, instant: bool = True):
        sqr = pygame.Rect((self.cordx, self.cordy), (self.side_len, self.side_len))
        pygame.draw.rect(self.screen, self.color, sqr, 1, border_radius=2)
        self.surface = sqr
        if self.mark == 1:
            img = pygame.image.load("icons8-finish-flag-50.png")
            img = pygame.transform.scale(img, (self.side_len - 4, self.side_len - 4))
            self.screen.blit(img, (self.cordx + 2, self.cordy + 2))
        elif self.mark == -1:
            img = pygame.image.load("icons8-play-50.png")
            img = pygame.transform.scale(img, (self.side_len - 4, self.side_len - 4))
            self.screen.blit(img, (self.cordx + 2, self.cordy + 2))
        elif self.mark == 2:
            pygame.draw.rect(self.screen, self.color, sqr, 0, border_radius=2)
        elif self.mark == -2:
            pygame.draw.rect(self.screen, GREY_COLOR, sqr, 0, border_radius=2)
        if not instant:
            pygame.display.update()

    def change_pos(self, x, y):
        self.cordx += x if self.cordx > -100 else 0
        self.cordy += y if self.cordy > -100 else 0

    def change_width(self, chg):
        self.side_len += chg
        self.cordx = self.row * self.side_len + self.row
        self.cordy = self.col * self.side_len + self.col
        return chg

    def mark_cell(self, new):
        self.mark = new

    def get_mark(self):
        return self.mark

