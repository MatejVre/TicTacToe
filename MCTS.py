from Node import Node
import functions
import random
import math

class MCTS():

    def __init__(self, root : Node):
        self.root = root

    def backpropagate(self, node : Node, value):
        node.update_value(value)
        if node.has_parent():
            self.backpropagate(node.get_parent(), value)

    def expand(self, node : Node):
        ns = functions.next_states(node.get_state())
        for state in ns:
            n = Node(0, 0, state, node)
            node.add_child(n)
        return node.get_children()[random.randint(0, len(node.get_children())-1)]
        
    def rollout(self, node : Node):
        state = node.get_state()
        check = functions.is_final_state(state)
        if check[0]:
            return check[1]
        while True:
            ns = functions.next_states(state)
            if len(ns) == 1:
                state = ns[0]
            else:
                state = ns[random.randint(0, len(ns)-1)]
            check = functions.is_final_state(state)
            if check[0]:
                return check[1]
    
    def select(self):
        node = self.root
        while node.has_children():
            ucbs = [self.upper_confidence_bound(child) for child in node.get_children()]
            maximum = max(ucbs)
            index = ucbs.index(maximum)
            new_node = node.get_children()[index]
            node = new_node
        return node

    def upper_confidence_bound(self, node : Node):
        v = node.get_v()
        n = node.get_n()
        if n == 0:
            return math.inf
        return ((v/n) + 1.44 * math.sqrt(math.log(self.root.get_n())/n))
    
    def calculate_move_tree(self):
        for _ in range(10000):
            node = self.select()
            if node.get_n() != 0 and functions.is_final_state(node.get_state())[0] == False:
                node = self.expand(node)
            rollout_value = self.rollout(node)
            self.backpropagate(node, rollout_value)
    
    def get_move(self):
        children = self.root.get_children()
        ucbs = [child.get_v() for child in children]
        maximum = min(ucbs)
        index = ucbs.index(maximum)
        node = children[index]
        return(functions.figure_out_move(self.root.get_state(), node.get_state()))