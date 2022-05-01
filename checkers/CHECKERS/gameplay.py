import pygame
from .constants import RED, WHITE, SQUARE_SIZE, BLUE, GREY
from .board import Board


class Game:
    def __init__(self, win):
        self._init()
        self.win = win

    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    # private method
    def _init(self):
        self.selected = None
        self.board = Board()
        # print(self.board)
        self.turn = RED
        self.valid_moves = {}

    def winner(self):
        return self.board.winner()

    def undo_move(self):
        return self.board.get_all_pieces(self.turn)

    # reset the game
    def reset(self):
        self._init()

    def select(self, row, col):
        # если нажали на шашку
        if self.selected:
            # пробуем его сдвинуть
            result = self._move(row, col)
            # если туда, куда мы нажали НЕЛЬЗЯ сдвинуть
            if not result:
                # делаем новый выбор
                self.selected = None
                self.select(row, col)

        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True
        return False

    # private method
    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        # если выбрали такой квадрат где нет другой шашки
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            # двигаем шашку в выбранный квадрат
            self.board.move(self.selected, row, col)
            pygame.draw.circle(self.win, GREY, (col * SQUARE_SIZE + SQUARE_SIZE // 2,
                                                row * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE * 2)
            skipped = self.valid_moves[(row, col)]

            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False

        return True

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE//2,
                                                row * SQUARE_SIZE + SQUARE_SIZE//2), 15)

    def change_turn(self):
        self.valid_moves = {}
        if self.turn == WHITE:
            self.turn = RED
        else:
            self.turn = WHITE

    def get_board(self):
        return self.board

    def ai_move(self, board):
        self.board = board
        self.change_turn()
