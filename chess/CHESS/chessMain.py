#!usr/bin/env python3
"""
user input and display
"""
from chess.CHESS.chessconstants import WIDTH, HEIGHT, WHITE, Board, rect, BLACK, GREY
import pygame
from chess.CHESS.chesspieces import chessPiece, Bishop
from chess.CHESS.chessboard import chessBoard
import time
from chess.CHESS.client import Network
import pickle
import os


chessbg = pygame.transform.scale(pygame.image.load(os.path.join("chess", "CHESS", "images", "chessbg.png")), (800, 800))

pygame.font.init()
turn = WHITE
FPS = 10


def menu_screen(win, name):
    global play, chessbg
    run = True
    offline = False

    while run:
        win.blit(chessbg, (0, 0))
        small_font = pygame.font.SysFont("comicsans", 50)

        if offline:
            off = small_font.render("Server Offline, Try Again Later...", 1, (255, 0, 0))
            win.blit(off, (WIDTH / 2 - off.get_width() / 2, 500))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                offline = False
                try:
                    play = connect()
                    run = False
                    chessgame()
                    break
                except:
                    print("Server Offline")
                    offline = True

'''
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

def connect():
    global n
    n = Network()
    return n.board

def chessgame():
    global play, turn, name, p1Time, p2Time

    color = play.start_user
    count = 0

    play = n.send("update_moves")
    play = n.send("name " + name)
    # p1Time = 900
    # p2Time = 900
    # turn = WHITE
    # count = 0
    # play = chessBoard(8, 8)
    # play.update_moves()
    clock = pygame.time.Clock()
    run = True
    # startTime = time.time()
    while run:
        if not color == "s":
            p1Time = play.time1
            p2Time = play.time2
            if count == 60:
                play = n.send("get")
                count = 0
            else:
                count += 1
        clock.tick(30)

        try:
            redraw_gameWindow(win, play, p1Time, p2Time,  color, play.ready)
        except Exception as e:
            print(e)
            end_screen(win, "Other player left")
            run = False
            break

        if not color == "s":
            if p1Time <= 0:
                play = n.send("winner b")
            elif p2Time <= 0:
                play = n.send("winner w")
            if play.check_mate(BLACK):
                play = n.send("winner b")
            elif play.check_mate(WHITE):
                play = n.send("winner w")

        if play.winner == WHITE:
            end_screen(win, "White is the winner!")
            run = False
        elif play.winner == BLACK:
            end_screen(win, "Black is the winner!")
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q and color != "s":
                    if color == WHITE:
                        play = n.send("winner b")
                    else:
                        play = n.send("winner w")
                if event.key == pygame.K_RIGHT:
                    play = n.send("forward")

                if event.key == pygame.K_LEFT:
                    play = n.send("back")

            if event.type == pygame.MOUSEBUTTONDOWN and color != "s":
                if color == play.turn and play.ready:

                # if color == turn:
                    pos = pygame.mouse.get_pos()
                    play = n.send("update moves")
                    i, j = click(pos)
                    # change = play.select(i, j, turn)
                    play = n.send("select" + str(i) + " " + str(j) + " " + color)
                '''
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
                '''
        n.disconnect()
        play = 0
        menu_screen(win, name)


name = input("Please type your nickname: ")
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Chess')
menu_screen(win, name)




