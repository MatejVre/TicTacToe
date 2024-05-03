from game import Game
from minmax import MinMax
import numpy as np
import random
from Node import Node
from MCTS import MCTS
game = Game()
minmax = MinMax()

turn = "X"

#game loop for playing MCTS
while True:
    row = None
    column = None
    played = False
    game.print_game_state()
    print(f"Player {turn} plays")
    if turn == "X":
        while not played:
            row = None
            column = None
            while row == None:
                row = input("Row:")
                if row not in ["0", "1", "2"]:
                    row = None
                    print("Pick 0, 1 or 2")
            while column == None:
                column = input("column:")
                if column not in ["0", "1", "2"]:
                    column1 = None
                    print("Pick 0, 1 or 2")
            played = game.play_move(turn, int(row), int(column))
    else:
        root = Node(0, 0, game.game_state)
        mcts = MCTS(root)
        mcts.calculate_move_tree()
        move = mcts.get_move()
        row = move[0]
        column = move[1]
        game.play_move(turn, int(row), int(column))
    check = game.check_winner()
    if check[0]:
        game.print_game_state()
        if check[1] == 1:
            print("X wins!")
        elif check[1] == -1:
            print("O wins!")
        else:
            print("Draw")
        break
    turn = "O" if turn == "X" else "X"

"""
while True:
    row = None
    column = None
    played = False
    game.print_game_state()
    print(f"Player {turn} plays")
    while not played:
        row = None
        column = None
        while row == None:
            row = input("Row:")
            if row not in ["0", "1", "2"]:
                row = None
                print("Pick 0, 1 or 2")
        while column == None:
            column = input("Row:")
            if column not in ["0", "1", "2"]:
                column1 = None
                print("Pick 0, 1 or 2")
        played = game.play_move(turn, int(row), int(column))
    check = game.check_winner()
    if check[0]:
        game.print_game_state()
        if check[1] == 1:
            print("X wins!")
        elif check[1] == -1:
            print("O wins!")
        else:
            print("Draw")
        break
    turn = "O" if turn == "X" else "X"
"""
#gameloop for playing minmax
"""
while True:
    row = None
    column = None
    played = False
    game.print_game_state()
    print(f"Player {turn} plays")
    if turn == "X":
        while not played:
            row = None
            column = None
            while row == None:
                row = input("Row:")
                if row not in ["0", "1", "2"]:
                    row = None
                    print("Pick 0, 1 or 2")
            while column == None:
                column = input("Row:")
                if column not in ["0", "1", "2"]:
                    column1 = None
                    print("Pick 0, 1 or 2")
            played = game.play_move(turn, int(row), int(column))
    else:
        states = {}
        winning_moves = []
        draw_moves = []
        losing_moves = []
        for s in minmax.next_states(game.game_state):
            states[minmax.figure_out_move(game.game_state,s)] = minmax.min_value(s)
        for key, value in states.items():
            if value == -1:
                winning_moves.append(key)
            elif value == 1:
                losing_moves.append(key)
            else:
                draw_moves.append(key)
        if winning_moves != []:
            move = winning_moves[0]
        elif draw_moves != []:
            move = draw_moves[0]
        else:
            move = losing_moves[0]
        row = move[0]
        column = move[1]
        game.play_move(turn, int(row), int(column))
    check = game.check_winner()
    if check[0]:
        game.print_game_state()
        if check[1] == 1:
            print("X wins!")
        elif check[1] == -1:
            print("O wins!")
        else:
            print("Draw")
        break
    turn = "O" if turn == "X" else "X"
"""