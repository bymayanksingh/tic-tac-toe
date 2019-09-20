import math
import sys

import pygame
from numpy import zeros

from assets import *
from config import *

pygame.init()
pygame.display.set_caption("Tic Tac Toe | Mayank Singh")
screen = pygame.display.set_mode(size)
screen.fill(white)


square = [[0 for i in range(3)] for j in range(3)]
for c in range(cols):
    for r in range(rows):
        square[r][c] = pygame.Rect(
            r * squaresize, c * squaresize, squaresize, squaresize
        )


def nought(x, y):
    screen.blit(noughtimg, (x, y))


def cross(x, y):
    screen.blit(crossimg, (x, y))


def winning_move(board, piece):
    for c in range(cols - 2):
        for r in range(rows):
            if (
                board[r][c] == piece
                and board[r][c + 1] == piece
                and board[r][c + 2] == piece
            ):
                return True

    for c in range(cols):
        for r in range(rows - 2):
            if (
                board[r][c] == piece
                and board[r + 1][c] == piece
                and board[r + 2][c] == piece
            ):
                return True

    for r in range(rows - 2):  # 0
        if (
            board[r][2 - r] == piece
            and board[r + 1][2 - r - 1] == piece
            and board[r + 2][2 - r - 2] == piece
        ):
            return True

    for c in range(cols - 2):
        for r in range(rows - 2):
            if (
                board[r][c] == piece
                and board[r + 1][c + 1] == piece
                and board[r + 2][c + 2] == piece
            ):
                return True


def draw_board(board):
    for c in range(cols):
        for r in range(rows):
            pygame.draw.rect(screen, black, square[r][c], 8)
    pygame.display.update()

    for c in range(cols):
        for r in range(rows):
            if board[r][c] == 1:
                nought(int(c * squaresize) + 6, int(r * squaresize) + 6)
            elif board[r][c] == 2:
                cross(int(c * squaresize) + 5, int(r * squaresize) + 5)
    pygame.display.update()


def create_board():
    board = zeros((rows, cols))
    return board


def play_move(board, row, col, piece):
    board[row][col] = piece


def is_valid_location(board, row, col):
    return board[row][col] == 0


def print_board(board):
    print(board)
    print(" ----------")
    print(" " + str([1, 2, 3]))
    print()


board = create_board()
draw_board(board)
print_board(board)


while not game_over:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if turn == 0:  # disc
                posx = event.pos[0]
                posy = event.pos[1]
                row = int(math.floor(posy / squaresize))
                col = int(math.floor(posx / squaresize))
                print(row, col)
                if is_valid_location(board, row, col):
                    play_move(board, row, col, 1)
                    turn += 1
                    turn = turn % 2
                print_board(board)
                draw_board(board)
                if winning_move(board, 1):
                    game_over = True
            else:
                posx = event.pos[0]
                posy = event.pos[1]
                row = int(math.floor(posy / squaresize))
                col = int(math.floor(posx / squaresize))
                print(row, col)
                if is_valid_location(board, row, col):
                    play_move(board, row, col, 2)
                    turn += 1
                    turn = turn % 2
                print_board(board)
                draw_board(board)
                if winning_move(board, 2):
                    game_over = True

        if game_over:
            pygame.time.wait(3000)
