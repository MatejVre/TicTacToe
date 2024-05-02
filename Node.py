#This class will be used to build up a tree for MCTS
#Will need:
#value -v
#num trials - n
#state - state (this will be the array)


class Node:

    def __init__(self, v, n, state, parent=None):
        self.v = v
        self.n = n
        self.state = state
        self.parent = parent
        self.children = []
    
    def add_child(self, child):
        self.children.append(child)
    
    def get_children(self):
        return self.children
    
    def update_value(self, value):
        self.v += value