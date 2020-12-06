# Locating the empty spaces on the board

import numpy as np

gamearr = np.array([[" ", " ", " "],
                    [" ", " ", " "],
                    [" ", " ", " "]])


def printboard(board):
    for i in range(np.size(gamearr[0])):
        if i != 0:
            print("---------")
        print(f"{board[i][0]} | {board[i][1]} | {board[i][2]}")


printboard(gamearr)


def rulestowin(board):
    n = 3
    for i in range(n):
        for j in range(n):
            if board[i][0] == board[i][1] == board[i][2]:
                return board[i][0]
            if board[0][j] == board[1][j] == board[2][j]:
                return board[0][j]
            # looking at the diagonal options
            if board[0][0] == board[1][1] == board[2][2]:
                return board[0][0]
            if board[0][2] == board[1][1] == board[0][2]:
                return board[0][2]


def character():
    print("Hello player 1, select your character to begin: ")

    class Character:
        nought = "o"
        crosses = "x"
        empty = ""

    character = input("X or O?")

    if character == 'x'.upper():
        print("Player 1: You have selected crosses. Begin")

    if character == 'o'.upper():
        print("Player 1: You have selected noughts. Begin")

    while character != Character.crosses and character != Character.nought:
        print("Player 1: Please select a valid character to start")
        break


def player1(character_input, gamearr):
    player = input('Make your move [0-9]')
    player = character_input
    if (gamearr[player-1]!0)



def minimax():
    return True
