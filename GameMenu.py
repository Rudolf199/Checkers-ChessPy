import pygame
import subprocess
from startbutton import StartButton
import sys

pygame.init()
pygame.font.init()

GREY = (128, 128, 128)
LIGHT = (211, 211, 211)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
cb_size = 180
bg_size = 640
c_x1_cord = 475
c_x2_cord = 135
c_y_cord = 300
c_radius = 80
c_deltax = 95
c_dinamic = 7
cb = pygame.transform.scale(pygame.image.load("menupics/" + 'chess' + ".png"), (cb_size, cb_size))
ckb = pygame.transform.scale(pygame.image.load("menupics/" + 'checkerchik' + ".png"), (cb_size, cb_size))
bg = pygame.transform.scale(pygame.image.load("menupics/" + "bg" + ".png"), (bg_size, bg_size))
win = pygame.display.set_mode((bg_size, bg_size))
pygame.display.set_caption('Game')
chess = StartButton(cb, c_x1_cord, c_y_cord, c_radius, GREY, WHITE, c_deltax, c_deltax, c_dinamic)
checkers = StartButton(ckb, c_x2_cord, c_y_cord, c_radius, GREY, WHITE, c_deltax, c_deltax, c_dinamic)
clock = pygame.time.Clock()


def drawtext(win, text, textcolor, rectcolor, x, y, fsize):
    # basic text drawing method, for nickname, income, etc
    font = pygame.font.SysFont('comicsans', fsize)
    text = font.render(text, True, textcolor, rectcolor)
    textRect = text.get_rect()
    textRect.center = (x, y)
    win.blit(text, textRect)


k = 0

edge = 300
fontsize = 30
edge_y = 100
FPS = 60

def main():
    global k
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
                # sys.exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = pygame.mouse.get_pos()[0]
                if x >= edge:
                    chess.clicked()
                    for i in range(5):
                        print("loading game in: ", i)
                    k = 2
                else:
                    checkers.clicked()
                    for i in range(5):
                        print("loading game in: ", i)
                    k = 1
        win.fill('#DCDDD8')
        win.blit(bg, (0, 0))
        drawtext(win, "Play Chess", LIGHT, BLACK, c_x1_cord, edge_y, fontsize)
        drawtext(win, "Play Checkers", LIGHT, BLACK, c_x2_cord, edge_y, fontsize)
        chess.draw(win)
        checkers.draw(win)
        pygame.display.update()
        clock.tick(FPS)

        if k == 1:
            subprocess.call(['python', 'checkers/checkers.py'])
            pygame.quit()
            run = False
        elif k == 2:
            subprocess.call(['python', 'chess/CHESS/chessMain.py'])
            pygame.quit()
            run = False
    # pygame.quit()
    # sys.exit(0)


main()
