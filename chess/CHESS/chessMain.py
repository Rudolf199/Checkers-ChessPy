#!usr/bin/env python3
"""
user input and display
"""
from chess.CHESS.chessconstants import WIDTH, HEIGHT, WHITE, Board, rect, BLACK, GREY
import pygame
from chess.CHESS.chesspieces import chessPiece, Bishop
from chess.CHESS.chessboard import chessBoard
import time
# from client import Network
import pickle


pygame.font.init()
turn = WHITE
FPS = 10


def redraw_gameWindow(win, play, p1, p2, color): # fix this with screenshot

    win.blit(Board, (0, 0))
    play.draw(win, color)
    formatTime1 = str(int(p1//60)) + ":" + str(int(p1%60))
    formatTime2 = str(int(p2//60)) + ":" + str(int(p2%60))
    if int(p1%60) < 10:
        formatTime1 = formatTime1[:-1] + "0" + formatTime1[-1]
    if int(p2%60) < 10:
        formatTime2 = formatTime2[:-1] + "0" + formatTime2[-1]
    font = pygame.font.SysFont("comicsans", 30)
    txt = font.render(play.p1Name + "\'s Time: " + str(formatTime2), 1, WHITE)
    txt2 = font.render(play.p2Name + "\'s Time: " + str(formatTime1), 1, WHITE)
    win.blit(txt, (520, 10))
    win.blit(txt2, (520, 700))
    pygame.display.update()



def end_screen(win, text):
    pygame.font.init()
    font = pygame.font.SysFont("comicsans", 80)
    txt = font.render(text, 1, (255, 0, 0))
    win.blit(txt, (WIDTH / 2 - txt.get_width() / 2, 300))
    pygame.display.update()

    pygame.time.set_timer(pygame.USEREVENT + 1, 3000)

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


def click(pos):
    x = pos[0]
    y = pos[1]
    if rect[0] < x < rect[0] + rect[2]:
        if rect[1] < y < rect[1] + rect[3]:
            divX = x - rect[0]
            divY = y - rect[1]
            i = int(divX / (rect[2]/8))
            j = int(divY / (rect[3]/8))
            #print(i, j)
            return i, j

    return -1, -1
def chessgame():
    global play
    p1Time = 900
    p2Time = 900
    turn = WHITE
    count = 0
    play = chessBoard(8, 8)
    play.update_moves()
    clock = pygame.time.Clock()
    run = True
    startTime = time.time()
    while run:
        clock.tick(30)
        color = turn
        if turn == WHITE:
            p1Time -= (time.time() - startTime)
            if p1Time <= 0:
                end_screen(win, "Black Won!!")
        else:
            p2Time -= (time.time() - startTime)
            if p2Time <= 0:
                end_screen(win, "White Won!!")
        startTime = time.time()
        redraw_gameWindow(win, play, int(p1Time), int(p2Time), color)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # if color == turn:
                pos = pygame.mouse.get_pos()
                play.update_moves()
                i, j = click(pos)
                change = play.select(i, j, turn)
                play.update_moves()
                if change == True:
                    startTime = time.time()
                    count += 1
                    if turn == WHITE:
                        turn = BLACK
                        #turn = BLACK
                        play.reset_selected()
                    else:
                        turn  = WHITE #play.turn
                        #turn = WHITE
                        play.reset_selected()

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Chess')
chessgame()




