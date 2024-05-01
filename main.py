from game import Game
from minmax import MinMax
import numpy as np

game = Game()
minmax = MinMax()

turn = "X"


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
