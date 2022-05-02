#!usr/bin/env python3
"""
user input and display
"""
from chess.CHESS.chessconstants import WIDTH, HEIGHT, WHITE, Board, rect, BLACK, chessbg, RED, all_time, TIME
from chess.CHESS.chessconstants import text_y1, text_x, text_y2, minute, minute2, size, title_size, menu_size
import pygame
from chess.CHESS.chesspieces import ChessPiece, Bishop
from chess.CHESS.chessboard import ChessBoard
import time

print("Enter first name: ")
name1 = str(input())
print("Enter second name: ")
name2 = str(input())

pygame.font.init()
turn = WHITE
FPS = 10
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Chess')


def menu_screen(win):
    # global play
    run = True
    while run:
        win.blit(chessbg, (0, 0))
        font = pygame.font.SysFont("comicsans", menu_size)
        title = font.render("Click to play Chess", True, WHITE)
        win.blit(title, (WIDTH / 2 - title.get_width() / 2, title_size))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False
    chessgame()


def redraw_gamewindow(win, play, p1, p2, color):  # fix this with screenshot

    win.blit(Board, (0, 0))
    play.draw(win, color)
    formatTime1 = str(int(p1 // minute)) + ":" + str(int(p1 % minute))
    formatTime2 = str(int(p2 // minute)) + ":" + str(int(p2 % minute))
    if int(p1 % minute) < minute2:
        formatTime1 = formatTime1[:-1] + "0" + formatTime1[-1]
    if int(p2 % minute) < minute2:
        formatTime2 = formatTime2[:-1] + "0" + formatTime2[-1]
    font = pygame.font.SysFont("comicsans", size)
    txt = font.render(play.p1Name + "\'s Time: " + str(formatTime2), True, WHITE)
    txt2 = font.render(play.p2Name + "\'s Time: " + str(formatTime1), True, WHITE)
    win.blit(txt, (text_x, text_y1))
    win.blit(txt2, (text_x, text_y2))
    pygame.display.update()


'''
def redraw_gameWindow(win, bo, p1, p2, color, ready):
    win.blit(Board, (0, 0))
    bo.draw(win, color)

    formatTime1 = str(int(p1//60)) + ":" + str(int(p1%60))
    formatTime2 = str(int(p2 // 60)) + ":" + str(int(p2 % 60))
    if int(p1 % 60) < 10:
        formatTime1 = formatTime1[:-1] + "0" + formatTime1[-1]
    if int(p2 % 60) < 10:
        formatTime2 = formatTime2[:-1] + "0" + formatTime2[-1]

    font = pygame.font.SysFont("comicsans", 30)
    try:
        txt = font.render(bo.p1Name + "\'s Time: " + str(formatTime2), 1, (255, 255, 255))
        txt2 = font.render(bo.p2Name + "\'s Time: " + str(formatTime1), 1, (255,255,255))
    except Exception as e:
        print(e)
    win.blit(txt, (520,10))
    win.blit(txt2, (520, 700))

    txt = font.render("Press q to Quit", 1, (255, 255, 255))
    win.blit(txt, (10, 20))

    if color == "s":
        txt3 = font.render("SPECTATOR MODE", 1, (255, 0, 0))
        win.blit(txt3, (WIDTH / 2 - txt3.get_width() / 2, 10))

    if not ready:
        show = "Waiting for Player"
        if color == "s":
            show = "Waiting for Players"
        font = pygame.font.SysFont("comicsans", 80)
        txt = font.render(show, 1, (255, 0, 0))
        win.blit(txt, (WIDTH / 2 - txt.get_width() / 2, 300))

    if not color == "s":
        font = pygame.font.SysFont("comicsans", 30)
        if color == WHITE:
            txt3 = font.render("YOU ARE WHITE", 1, (255, 0, 0))
            win.blit(txt3, (WIDTH / 2 - txt3.get_width() / 2, 10))
        else:
            txt3 = font.render("YOU ARE BLACK", 1, (255, 0, 0))
            win.blit(txt3, (WIDTH / 2 - txt3.get_width() / 2, 10))

        if bo.turn == color:
            txt3 = font.render("YOUR TURN", 1, (255, 0, 0))
            win.blit(txt3, (WIDTH / 2 - txt3.get_width() / 2, 700))
        else:
            txt3 = font.render("THEIR TURN", 1, (255, 0, 0))
            win.blit(txt3, (WIDTH / 2 - txt3.get_width() / 2, 700))

    pygame.display.update()
'''


def end_screen(win, text):
    pygame.font.init()
    font = pygame.font.SysFont("comicsans", menu_size)
    txt = font.render(text, True, RED)
    win.blit(txt, (WIDTH / 2 - txt.get_width() / 2, 2 * title_size))
    pygame.display.update()

    pygame.time.set_timer(pygame.USEREVENT + 1, all_time)
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
            i = int(divX / (rect[2] / 8))
            j = int(divY / (rect[3] / 8))
            # print(i, j)
            return i, j

    return -1, -1


'''
def connect():
    global n
    n = Network()
    return n.board
'''


def chessgame():
    global play
    p1Time = TIME
    p2Time = TIME
    turn = WHITE
    count = 0
    play = ChessBoard(8, 8, name1, name2)
    play.update_moves()
    clock = pygame.time.Clock()
    run = True
    startTime = time.time()
    while run:
        clock.tick(size)
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
        redraw_gamewindow(win, play, int(p1Time), int(p2Time), color)
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
                # change = play.select(i, j, play.turn)
                if change is True:
                    startTime = time.time()
                    count += 1
                    if turn == WHITE and not play.is_checked(turn):
                        turn = BLACK
                        play.reset_selected()
                    elif turn == WHITE and play.is_checked(turn):
                        turn = WHITE  # play.turn
                        # turn = WHITE
                        play.reset_selected()
                    elif turn == BLACK and not play.is_checked(turn):
                        turn = WHITE
                        play.reset_selected()
                    elif turn == BLACK and play.is_checked(turn):
                        turn = BLACK
                        play.reset_selected()
                    elif turn == WHITE and play.is_checked(turn) and play.check_mate(turn):
                        end_screen(win, "Black Won!!")
                    elif turn == BLACK and play.is_checked(turn) and play.check_mate(turn):
                        end_screen(win, "White Won!!")
    menu_screen(win)


menu_screen(win)
