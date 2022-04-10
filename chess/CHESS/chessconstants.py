import pygame
import os


WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS
WHITE = (255, 255, 255)
GREY = (128,128,128)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
rect = (118, 120, 565, 565)
Board = pygame.transform.scale(pygame.image.load(os.path.join("images", "board_alt.png")), (800, 800))
b_bishop = pygame.transform.scale(pygame.image.load("images/" + 'bB' + ".png"), (70, 65))
b_king = pygame.transform.scale(pygame.image.load("images/" + 'bK' + ".png"), (70, 70))
b_knight = pygame.transform.scale(pygame.image.load("images/" + 'bN' + ".png"), (70, 70))
b_pawn = pygame.transform.scale(pygame.image.load("images/" + 'bp' + ".png"), (70, 70))
b_queen = pygame.transform.scale(pygame.image.load("images/" + 'bQ' + ".png"), (70, 70))
b_rook = pygame.transform.scale(pygame.image.load("images/" + 'bR' + ".png"), (70, 70))

w_bishop = pygame.transform.scale(pygame.image.load("images/" + 'wB' + ".png"), (70, 60))
w_king = pygame.transform.scale(pygame.image.load("images/" + 'wK' + ".png"), (70, 55))
w_knight = pygame.transform.scale(pygame.image.load("images/" + 'wN' + ".png"), (70, 55))
w_pawn = pygame.transform.scale(pygame.image.load("images/" + 'wp' + ".png"), (70, 55))
w_queen = pygame.transform.scale(pygame.image.load("images/" + 'wQ' + ".png"), (70, 55))
w_rook = pygame.transform.scale(pygame.image.load("images/" + 'wR' + ".png"), (70, 55))

B = [b_bishop, b_king, b_knight, b_pawn, b_queen, b_rook]
W = [w_bishop, w_king, w_knight, w_pawn, w_queen, w_rook]
