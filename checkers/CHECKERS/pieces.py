import pygame
from .constants import RCROWN, UCROWN, RED, WHITE, GREY, SQUARE_SIZE


class Piece:
    PADDING = 15
    OUTLINE = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        # пусть красные идут наверх => направление отрицательное
        # if self.color == RED:
        #   self.direction = -1
        # else:
        #   self.direction = 1
        # self.x = 0
        # self.y = 0
        self.calc_pos()
        # так как центр шашки совпадает с центром квадрата, надо найти центр квадрата, это и будет координатами шашки

    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king(self):
        self.king = True
    # рисуем шашки, в виде одного кружка внутри другого

    def draw(self, win):
        radius = SQUARE_SIZE//2 - self.PADDING
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.OUTLINE)  # большой кпужок
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)  # маленький куржой
        if self.king and self.color == RED:
            # blit import image on display
            win.blit(RCROWN, (self.x - RCROWN.get_width()//2, self.y - RCROWN.get_height()//2))
        elif self.king and self.color == WHITE:
            win.blit(UCROWN, (self.x - UCROWN.get_width() // 2, self.y - UCROWN.get_height() // 2))

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()
    # def __repr__(self):
    #    return str(self.color)
