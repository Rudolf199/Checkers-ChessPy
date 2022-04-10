import pygame as pg
import checkers
import chess
from chess.CHESS import chessMain
pg.init()
color_light = (170,170,170)
color_dark = (100,100,100)
class Window:
    res = (1080, 720)

    def __init__(self):
        self.screen = pg.display.set_mode((720, 720))
        self.height = self.screen.get_height()
        self.width = self.screen.get_width()
        self.rect = self.screen.get_rect()
        self.FPS = 30
        self.clock = pg.time.Clock()
        self.font = pg.font.SysFont("comicsans", 25)
        self.menu_open = True
        self.colors = {"red": (255, 0, 0),
                       "green": (0, 255, 0),
                       "blue": (0, 0, 255)}

    def setup(self):
        self.screen.fill(self.colors["black"])
        pg.display.set_caption("Main Menu!")

    def text(self, message, text_color, x_pos, y_pos):
        text = self.font.render(message, True, (self.colors[text_color]))
        text_rect = text.get_rect(center=(x_pos, y_pos))
        self.screen.blit(text, text_rect)

    def exit(self):
        self.screen.fill(self.colors["black"])
        text = self.font.render("Thank you for playing. Goodbye!", True,
                                (self.colors["white"]))
        text_rect = text.get_rect(center=(self.rect.w/2, self.rect.h/2))
        self.screen.blit(text, text_rect)
        pg.display.update()
        pg.time.wait(1000)
        pg.quit()
        sys.exit()

def main():
    win = Window()
    while True:
        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                pg.quit()
            if ev.type == pg.MOUSEBUTTONDOWN:
                if win.width / 2 <= mouse[0] <= win.width / 2 + 140 and win.height / 2 <= mouse[1] <= win.height / 2 + 40:
                    pg.quit()
        win.screen.fill((60, 25, 60))
        mouse = pg.mouse.get_pos()
        if win.width / 2 <= mouse[0] <= win.width / 2 + 140 and win.height / 2 <= mouse[1] <= win.height / 2 + 40:
            pg.draw.rect(win.screen, color_light, [win.width / 2, win.height / 2, 140, 40])
        else:
            pg.draw.rect(win.screen, color_dark, [win.width / 2, win.height / 2, 140, 40])
        win.screen.blit(win.text, (win.width / 2 + 50, win.height / 2))

        # updates the frames of the game
        pg.display.update()