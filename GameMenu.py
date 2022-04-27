import pygame
import subprocess
from startbutton import StartButton


pygame.init()
pygame.font.init()
GREY = (128, 128, 128)
LIGHT = (211, 211, 211)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
cb = pygame.transform.scale(pygame.image.load("menupics/" + 'chess' + ".png"), (180, 180))
ckb = pygame.transform.scale(pygame.image.load("menupics/" + 'checkerchik' + ".png"), (180, 180))
bg = pygame.transform.scale(pygame.image.load("menupics/" + "bg" + ".png"), (640, 640))
win = pygame.display.set_mode((640, 640))
pygame.display.set_caption('Game')
chess = StartButton(cb, 475, 300, 80, GREY, WHITE, 95, 95, 7)
checkers = StartButton(ckb, 135, 300, 80, GREY, WHITE, 95, 95, 7)
clock = pygame.time.Clock()


def drawtext(win, text, textcolor, rectcolor, x, y, fsize):
    # basic text drawing method, for nickname, income, etc
    font = pygame.font.SysFont('comicsans', fsize)
    text = font.render(text, True, textcolor, rectcolor)
    textRect = text.get_rect()
    textRect.center = (x, y)
    win.blit(text, textRect)


k = 0


def main():
    global k
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # pygame.quit()
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = pygame.mouse.get_pos()[0]
                if x >= 300:
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
        drawtext(win, "Play Chess", LIGHT, BLACK, 475, 100, 30)
        drawtext(win, "Play Checkers", LIGHT, BLACK, 135, 100, 30)
        chess.draw(win)
        checkers.draw(win)
        pygame.display.update()
        clock.tick(60)
        if k == 1:
            subprocess.call(['python', 'checkers/checkers.py'])
            run = False
        elif k == 2:
            subprocess.call(['python', 'chess/CHESS/chessMain.py'])
            run = False
    pygame.quit()


main()
