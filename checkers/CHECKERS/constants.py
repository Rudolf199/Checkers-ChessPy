import pygame
import os
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

# rgb
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)
GREEN = (0, 255, 0)
# грузим корону для дамки
RCROWN = pygame.transform.scale(pygame.image.load(os.path.join('checkers', 'CHECKERS',
                                                               'pics/crown.png')), (60, 70))
UCROWN = pygame.transform.scale(pygame.image.load(os.path.join("checkers", "CHECKERS",
                                                               "pics/usa_gerb_PNG3.png")), (60, 70))
Rsound = pygame.mixer.Sound(os.path.join('checkers', "CHECKERS", "sounds/russia.wav"))
Usound = pygame.mixer.Sound(os.path.join('checkers', "CHECKERS", "sounds/usa.wav"))

