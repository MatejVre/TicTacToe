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
        self.n += 1
    
    def has_parent(self):
        return self.parent != None
    
    def has_children(self):
        return self.children != []
    
    def get_parent(self):
        return self.parent
    
    def display(self):
        print(self.state, self.v, self.n)
    
    def get_state(self):
        return self.state

    def get_v(self):
        return self.v
    
    def get_n(self):
        return self.n
    