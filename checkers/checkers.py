#!usr/bin/env python3
import pygame
from CHECKERS.constants import WIDTH, HEIGHT, RED, WHITE, SQUARE_SIZE
from CHECKERS.gameplay import Game
from minimax.checkerbot import minimax

#import os
#os.environ["SDL_VIDEODRIVER"] = "dummy"
FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # display
pygame.display.set_caption('Checkers')

# чтобы двигать шашками мышкой
def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)


    while run:
        clock.tick(FPS)

        if game.turn == WHITE:
            value, new_board = minimax(game.get_board(), 4, WHITE, game)
            game.ai_move(new_board)


        if game.winner() == RED:
            for i in range(50):
                print(" RED won!!! ")
            run = False
        elif game.winner() == WHITE:
            for i in range(100):
                print(" WHITE won!!! ")
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()

    pygame.quit()

main()