import pygame
from chess.CHESS.chesspieces import Bishop, King, Rook, Pawn, Queen, Knight
from chess.CHESS.chessconstants import BLACK, WHITE
import time


class chessBoard:
    rect = (118, 120, 565, 565)
    startX = rect[0]
    startY = rect[1]
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

        self.ready = False

        self.last = None

        self.copy = True

        self.board = [[0 for x in range(8)] for _ in range(rows)]

        self.board[0][0] = Rook(0, 0, BLACK)
        self.board[0][1] = Knight(0, 1, BLACK)
        self.board[0][2] = Bishop(0, 2, BLACK)
        self.board[0][3] = Queen(0, 3, BLACK)
        self.board[0][4] = King(0, 4, BLACK)
        self.board[0][5] = Bishop(0, 5, BLACK)
        self.board[0][6] = Knight(0, 6, BLACK)
        self.board[0][7] = Rook(0, 7, BLACK)

        self.board[1][0] = Pawn(1, 0, BLACK)
        self.board[1][1] = Pawn(1, 1, BLACK)
        self.board[1][2] = Pawn(1, 2, BLACK)
        self.board[1][3] = Pawn(1, 3, BLACK)
        self.board[1][4] = Pawn(1, 4, BLACK)
        self.board[1][5] = Pawn(1, 5, BLACK)
        self.board[1][6] = Pawn(1, 6, BLACK)
        self.board[1][7] = Pawn(1, 7, BLACK)

        self.board[7][0] = Rook(7, 0, WHITE)
        self.board[7][1] = Knight(7, 1, WHITE)
        self.board[7][2] = Bishop(7, 2, WHITE)
        self.board[7][3] = Queen(7, 3, WHITE)
        self.board[7][4] = King(7, 4, WHITE)
        self.board[7][5] = Bishop(7, 5, WHITE)
        self.board[7][6] = Knight(7, 6, WHITE)
        self.board[7][7] = Rook(7, 7, WHITE) # glitchy piece

        self.board[6][0] = Pawn(6, 0, WHITE)
        self.board[6][1] = Pawn(6, 1, WHITE)
        self.board[6][2] = Pawn(6, 2, WHITE)
        self.board[6][3] = Pawn(6, 3, WHITE)
        self.board[6][4] = Pawn(6, 4, WHITE)
        self.board[6][5] = Pawn(6, 5, WHITE)
        self.board[6][6] = Pawn(6, 6, WHITE)
        self.board[6][7] = Pawn(6, 7, WHITE)
        self.p1Name = "Black"
        self.p2Name = "White"
        self.turn = WHITE
        self.time1 = 900
        self.time2 = 900
        self.storedTime1 = 0
        self.storedTime2 = 0
        self.winner = None
        self.startTime = time.time()

    def update_moves(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] != 0:
                    self.board[i][j].update_valid_moves(self.board) # find this
    #'''
    def draw(self, win, color):
        if self.last and color == self.turn:
            y, x = self.last[0]
            y1, x1 = self.last[1]

            xx = (4 - x) +round(self.startX + (x * self.rect[2] / 8))
            yy = 3 + round(self.startY + (y * self.rect[3] / 8))
            pygame.draw.circle(win, (0,0,255), (xx+32, yy+30), 34, 4)
            xx1 = (4 - x) + round(self.startX + (x1 * self.rect[2] / 8))
            yy1 = 3+ round(self.startY + (y1 * self.rect[3] / 8))
            pygame.draw.circle(win, (0, 0, 255), (xx1 + 20, yy1 + 20), 34, 4)

        s = None
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] != 0:
                    self.board[i][j].draw(win, color)
                    if self.board[i][j].isSelected:
                        s = (i, j)

    def get_danger_moves(self, color):
        danger_moves = []
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] != 0:
                    #self.board[i][j].draw(win, WHITE)
                    for move in self.board[i][j].move_list: #move_list??
                        danger_moves.append(move)
        return danger_moves


    def is_checked(self, color):
        self.update_moves()
        danger_moves = self.get_danger_moves(color)
        king_pos = (-1, -1)
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] != 0:
                    if self.board[i][j].king and self.board[i][j].color == color:
                        king_pos = (j, i)

        if king_pos in danger_moves:
            return True
        return False

    def check_mate(self, color):
        if self.is_checked(color):
                   king = None
                   for i in range(self.rows):
                       for j in range(self.cols):
                           if self.board[i][j] != 0:
                               if self.board[i][j].king and self.board[i][j].color == color:
                                   king = self.board[i][j]
                   if king is not None:
                       valid_moves = king.valid_moves(self.board)
                       danger_moves = self.get_danger_moves(color)
                       danger_count = 0
                       for move in valid_moves:
                           if move in danger_moves:
                               danger_count += 1
                       return danger_count == len(valid_moves)
        return False

    def reset_selected(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] != 0:
                    self.board[i][j].selected = False

    # correct one
    def select(self, col, row, color):
        changed = False
        prev = (-1, -1)
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] != 0:
                    if self.board[i][j].selected:
                        prev = (i, j)
        #if piece
        if self.board[row][col] == 0:
            print("type", type(self.board[prev[0]][prev[1]]))
            print(self.board[prev[0]][prev[1]])
            moves = self.board[prev[0]][prev[1]].move_list
            if (col, row) in moves:
                self.move(prev, (row, col), color)
                changed = True
                #changed = True
            self.reset_selected()
        else:
            print("typeik", type(self.board[prev[0]][prev[1]]))
            if self.board[prev[0]][prev[1]].color != self.board[row][col].color:
                print("qaq", self.board[prev[0]][prev[1]])
                moves = self.board[prev[0]][prev[1]].move_list
                if (col, row) in moves:
                    self.move(prev, (row, col), color)
                    changed = True
                self.reset_selected()
                if self.board[row][col].color == color:
                    self.board[row][col].selected = True
            else:
                self.reset_selected()
                if self.board[row][col].color == color:
                    self.board[row][col].selected = True
        return changed

    # correct one
    def move(self, start, end, color):
        checkedBefore = self.is_checked(color)
        changed = True
        nBoard = self.board[:]
        if nBoard[start[0]][start[1]].pawn:
            nBoard[start[0]][start[1]].first = False
        nBoard[start[0]][start[1]].change_pos((end[0], end[1]))
        nBoard[end[0]][end[1]] = nBoard[start[0]][start[1]]
        nBoard[start[0]][start[1]] = 0
        self.board = nBoard
        if self.is_checked(color) or (checkedBefore and self.is_checked(color)):
            changed = False
            nBoard = self.board[:]
            if nBoard[end[0]][end[1]].pawn:
                nBoard[end[0]][end[1]].first = True
            nBoard[end[0]][end[1]].change_pos((start[0], start[1]))
            nBoard[start[0]][start[1]] = nBoard[end[0]][end[1]]
            nBoard[end[0]][end[1]] = 0
            self.board = nBoard
        else:
            self.reset_selected()
        self.update_moves()
        if changed:
            self.last = [start, end]
            if self.turn == WHITE:
                self.storedTime1 += (time.time() - self.startTime)
            else:
                self.storedTime2 += (time.time() - self.startTime)
            self.startTime = time.time()
        return changed
