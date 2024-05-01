import numpy as np
import copy

class Game:

    def __init__(self):
        self.game_state = [["_", "_", "_"],
                            ["_", "_", "_"],
                            ["_", "_", "_"]]
        
        self.past_states = []

    def print_game_state(self):
        print(self.game_state[0])
        print(self.game_state[1])
        print(self.game_state[2])

    def play_move(self, player, row, column):
        #check the position isn't occupied
        if self.game_state[row][column] != "_":
            print("This space is already occupied")
            return False
        else:
            prev_state = copy.deepcopy(self.game_state)
            self.past_states.append(prev_state)
            self.game_state[row][column] = player
            return True

    def check_winner(self):
        for i in range(3):
            if self.game_state[i] == ["X", "X", "X"]:
                return True, 1
            elif self.game_state[i] == ["O", "O", "O"]:
                return True, -1
            elif (self.game_state[0][i] == "X") and (self.game_state[1][i] == "X") and (self.game_state[2][i] == "X"):
                return True, 1
            elif (self.game_state[0][i] == "O") and (self.game_state[1][i] == "O") and (self.game_state[2][i] == "O"):
                return True, -1
        if (self.game_state[0][0] == "X") and (self.game_state[1][1] == "X") and (self.game_state[2][2] == "X"):
            return True, 1
        elif (self.game_state[0][0] == "O") and (self.game_state[1][1] == "O") and (self.game_state[2][2] == "O"):
            return True, -1
        elif (self.game_state[0][2] == "X") and (self.game_state[1][1] == "X") and (self.game_state[2][0] == "X"):
            return True, 1
        elif (self.game_state[0][2] == "O") and (self.game_state[1][1] == "O") and (self.game_state[2][0] == "O"):
            return True, -1
        elif ("_" not in self.game_state[0]) and ("_" not in self.game_state[1]) and ("_" not in self.game_state[2]):
            return True, 0
        return False, None

    