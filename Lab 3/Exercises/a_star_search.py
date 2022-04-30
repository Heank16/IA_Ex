class Node:  # Node has only PARENT_NODE, STATE, DEPTH
    def __init__(self, state, parent=None, depth=0, pathCost=0):
        self.STATE = state
        self.PARENT_NODE = parent
        self.DEPTH = depth
        self.PATH_COST = pathCost

    def path(self):  # Create a list of nodes from the root to this node.
        current_node = self
        path = [self]
        while current_node.PARENT_NODE:  # while current node has parent
            current_node = current_node.PARENT_NODE  # make parent the current node
            path.append(current_node)  # add current node to path
        return path

    def display(self):
        print(self)

    def __repr__(self):
        return 'State: ' + str(self.STATE) + ' - Depth: ' + str(self.DEPTH)


# Search the tree for the goal state and return path from initial state to goal state
def TREE_SEARCH():
    fringe = []
    initial_node = Node(INITIAL_STATE)
    fringe = INSERT(initial_node, fringe)
    while fringe:
        node = REMOVE_NEXT(fringe)  # Get the node with the lowest cost, and remove it from fringe
        if node.STATE in GOAL_STATE:
            return node.path()
        children = EXPAND(node)  # Visit the node's children by expand
        fringe = INSERT_ALL(children, fringe)  # Add visited nodes to fringe
        print("fringe: {}".format(fringe))


# Expands node and gets the successors (children) of that node.
# Return list of the successor nodes.
def EXPAND(node):
    successors = []
    children = successor_fn(node.STATE)
    for child in children:
        s = Node(child[0], node, node.DEPTH + 1, node.PATH_COST + child[1])
        successors = INSERT(s, successors)
    return successors


# Insert node in to the queue (fringe).
def INSERT(node, queue):
    #queue.append(node)
    queue.insert(0, node)
    return queue


# Insert list of nodes into the fringe
def INSERT_ALL(list, queue):
    for node in list:
        INSERT(node, queue)
    return queue


# Removes and returns the best fit element from fringe
def REMOVE_NEXT(queue):
    best_fit_node = queue[0]
    i = 1
    while i < len(queue):
        if queue[i].STATE[1] + queue[i].PATH_COST <= best_fit_node.STATE[1] + best_fit_node.PATH_COST:
            best_fit_node = queue[i]
        i += 1

    return queue.pop(i - 1)


# Successor function, mapping the nodes to its successors
def successor_fn(state):  # Lookup list of successor states
    return STATE_SPACE[state]  # successor_fn( 'C' ) returns ['F', 'G']


INITIAL_STATE = ('A', 6)
GOAL_STATE = (('K', 0), ('L', 0))
STATE_SPACE = {
    ('A', 6): [(('B', 5), 1), (('C', 5), 2), (('D', 2), 4)],
    ('B', 5): [(('A', 6), 1), (('F', 5), 5), (('E', 4), 4)],
    ('C', 5): [(('A', 6), 2), (('E', 4), 1)],
    ('D', 2): [(('A', 6), 4), (('I', 2), 4), (('H', 1), 1), (('J', 1), 2)],
    ('E', 4): [(('B', 5), 4), (('C', 5), 1), (('G', 4), 2), (('H', 1), 3)],
    ('F', 5): [(('B', 5), 5), (('G', 4), 1)],
    ('G', 4): [(('F', 5), 1), (('E', 4), 2), (('K', 0), 6)],
    ('H', 1): [(('E', 4), 3), (('D', 2), 1), (('K', 0), 6), (('L', 0), 5)],
    ('I', 2): [(('D', 2), 4), (('L', 0), 3)],
    ('J', 1): [(('D', 2), 2)],
    ('K', 0): [(('G', 4), 6), (('H', 1), 6)],
    ('L', 0): [(('I', 2), 3), (('H', 1), 5)]
}


# Run tree search and display the nodes in the path to goal node
def run():
    path = TREE_SEARCH()
    print('Solution path:')
    for node in path:
        node.display()


if __name__ == '__main__':
    run()
