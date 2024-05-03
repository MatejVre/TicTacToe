import copy


def next_states(state):
        pl = player(state)
        states = []
        for i in range(3):
            for u in range(3):
                if state[i][u] == "_":
                    s = copy.deepcopy(state)
                    s[i][u] = pl
                    states.append(s)
        return states

def player(state):
        #count X's
        Xs = sum([x.count("X") for x in state])
        Os = sum([x.count("O") for x in state])
        calc = Xs - Os
        return "X" if calc == 0 else "O"
    
def figure_out_move(previous_state, current_state):
    for i in range(3):
        for u in range(3):
            if previous_state[i][u] != current_state[i][u]:
                return (i, u)

def is_final_state(state):
    for i in range(3):
        if state[i] == ["X", "X", "X"]:
            return True, 1
        elif state[i] == ["O", "O", "O"]:
            return True, -1
        elif (state[0][i] == "X") and (state[1][i] == "X") and (state[2][i] == "X"):
            return True, 1
        elif (state[0][i] == "O") and (state[1][i] == "O") and (state[2][i] == "O"):
            return True, -1
    if (state[0][0] == "X") and (state[1][1] == "X") and (state[2][2] == "X"):
        return True, 1
    elif (state[0][0] == "O") and (state[1][1] == "O") and (state[2][2] == "O"):
        return True, -1
    elif (state[0][2] == "X") and (state[1][1] == "X") and (state[2][0] == "X"):
        return True, 1
    elif (state[0][2] == "O") and (state[1][1] == "O") and (state[2][0] == "O"):
        return True, -1
    elif ("_" not in state[0]) and ("_" not in state[1]) and ("_" not in state[2]):
        return True, 0
    return False, None
