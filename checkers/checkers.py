#!usr/bin/env python3
import pygame
import os
from CHECKERS.constants import WIDTH, HEIGHT, RED, WHITE, SQUARE_SIZE, Rsound, Usound
from CHECKERS.gameplay import Game
from minimax.checkerbot import minimax
pygame.init()


FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # display
pygame.display.set_caption('Checkers')
checkersbg = pygame.transform.scale(pygame.image.load(os.path.join("checkers", "CHECKERS", "checkersbg.png")),
                                    (800, 800))


# чтобы двигать шашками мышкой
def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def menu_screen(win):
    global checkersbg
    run = True
    while run:
        win.blit(checkersbg, (0, 0))
        font = pygame.font.SysFont("comicsans", 80)
        title = font.render("Click to play Checkers", True, WHITE)
        win.blit(title, (WIDTH / 2 - title.get_width() / 2, 200))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False
    checkersgame()


def end_screen(win, text):
    pygame.font.init()
    font = pygame.font.SysFont("comicsans", 80)
    txt = font.render(text, True, WHITE)
    win.blit(txt, (WIDTH / 2 - txt.get_width() / 2, 300))
    pygame.display.update()
    run = True

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                run = False
            elif event.type == pygame.KEYDOWN:
                run = False
            elif event.type == pygame.USEREVENT + 1:
                run = False


def checkersgame():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
    while run:
        clock.tick(FPS)
        if game.turn == WHITE:
            value, new_board = minimax(game.get_board(), 4, WHITE, game)
            game.ai_move(new_board)
        if game.winner() == RED:
            Rsound.play()
            end_screen(WIN, "Red won")
            # run = False
        elif game.winner() == WHITE:
            Usound.play()
            end_screen(WIN, "White won")
            # run = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_l:
                    Rsound.play()
                if event.key == pygame.K_p:
                    Usound.play()
        game.update()

    pygame.quit()


menu_screen(WIN)
