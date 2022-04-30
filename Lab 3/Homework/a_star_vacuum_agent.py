#####################################
# Square ids
#####################################
A = 'A'
B = 'B'
C = 'C'
D = 'D'

#####################################
# A star
#####################################
# (Square, distance to goal square, (clean state))
INITIAL_STATE = (A, 1, ('Clean', 'Dirty', 'Dirty', 'Dirty'))
GOAL_STATE = (C, 0, ('Clean', 'Clean', 'Clean', 'Clean'))
STATE_SPACE = {
    # A
    (A, 1, ('Clean', 'Dirty', 'Dirty', 'Dirty')): [
        # ((Square, distance to goal square, (clean state)), cost)
        ((B, 2, ('Clean', 'Clean', 'Dirty', 'Dirty')), 1),
        ((C, 0, ('Clean', 'Dirty', 'Clean', 'Dirty')), 1)
    ],
    (A, 1, ('Clean', 'Clean', 'Dirty', 'Dirty')): [
        ((B, 2, ('Clean', 'Clean', 'Dirty', 'Dirty')), 1),
        ((C, 0, ('Clean', 'Clean', 'Clean', 'Dirty')), 1)
    ],
    (A, 1, ('Clean', 'Dirty', 'Clean', 'Dirty')): [
        ((B, 2, ('Clean', 'Clean', 'Clean', 'Dirty')), 1),
        ((C, 0, ('Clean', 'Dirty', 'Clean', 'Dirty')), 1)
    ],
    (A, 1, ('Clean', 'Clean', 'Clean', 'Dirty')): [
        ((B, 2, ('Clean', 'Clean', 'Clean', 'Dirty')), 1),
        ((C, 0, ('Clean', 'Clean', 'Clean', 'Dirty')), 1)
    ],
    (A, 1, ('Clean', 'Clean', 'Clean', 'Clean')): [
        ((B, 2, ('Clean', 'Clean', 'Clean', 'Clean')), 1),
        ((C, 0, ('Clean', 'Clean', 'Clean', 'Clean')), 1)
    ],
    (A, 1, ('Clean', 'Clean', 'Dirty', 'Clean')): [
        ((B, 2, ('Clean', 'Clean', 'Dirty', 'Clean')), 1),
        ((C, 0, ('Clean', 'Clean', 'Clean', 'Clean')), 1)
    ],
    (A, 1, ('Clean', 'Dirty', 'Clean', 'Clean')): [
        ((B, 2, ('Clean', 'Clean', 'Clean', 'Clean')), 1),
        ((C, 0, ('Clean', 'Dirty', 'Clean', 'Clean')), 1)
    ],

    # B
    (B, 2, ('Clean', 'Clean', 'Dirty', 'Dirty')): [
        ((A, 1, ('Clean', 'Clean', 'Dirty', 'Dirty')), 1),
        ((D, 1, ('Clean', 'Clean', 'Dirty', 'Clean')), 1)
    ],
    (B, 2, ('Clean', 'Clean', 'Dirty', 'Clean')): [
        ((A, 1, ('Clean', 'Clean', 'Dirty', 'Clean')), 1),
        ((D, 1, ('Clean', 'Clean', 'Dirty', 'Clean')), 1)
    ],
    (B, 2, ('Clean', 'Clean', 'Clean', 'Dirty')): [
        ((A, 1, ('Clean', 'Clean', 'Clean', 'Dirty')), 1),
        ((D, 1, ('Clean', 'Clean', 'Clean', 'Clean')), 1)
    ],
    (B, 2, ('Clean', 'Clean', 'Clean', 'Clean')): [
        ((A, 1, ('Clean', 'Clean', 'Clean', 'Clean')), 1),
        ((D, 1, ('Clean', 'Clean', 'Clean', 'Clean')), 1)
    ],

    # C
    (C, 0, ('Clean', 'Dirty', 'Clean', 'Dirty')): [
        ((A, 1, ('Clean', 'Dirty', 'Clean', 'Dirty')), 1),
        ((B, 2, ('Clean', 'Clean', 'Clean', 'Dirty')), 1)
    ],
    (C, 0, ('Clean', 'Clean', 'Clean', 'Dirty')): [
        ((A, 1, ('Clean', 'Clean', 'Clean', 'Dirty')), 1),
        ((B, 2, ('Clean', 'Clean', 'Clean', 'Dirty')), 1)
    ],
    (C, 0, ('Clean', 'Dirty', 'Clean', 'Clean')): [
        ((A, 1, ('Clean', 'Dirty', 'Clean', 'Clean')), 1),
        ((B, 2, ('Clean', 'Clean', 'Clean', 'Clean')), 1)
    ],
    (C, 0, ('Clean', 'Clean', 'Clean', 'Clean')): [
        ((A, 1, ('Clean', 'Clean', 'Clean', 'Clean')), 1),
        ((B, 2, ('Clean', 'Clean', 'Clean', 'Clean')), 1)
    ],

    # D
    (D, 1, ('Clean', 'Clean', 'Dirty', 'Clean')): [
        ((B, 2, ('Clean', 'Clean', 'Dirty', 'Clean')), 1),
        ((C, 0, ('Clean', 'Clean', 'Clean', 'Clean')), 1)
    ],
    (D, 1, ('Clean', 'Dirty', 'Clean', 'Clean')): [
        ((B, 2, ('Clean', 'Clean', 'Clean', 'Clean')), 1),
        ((C, 0, ('Clean', 'Dirty', 'Clean', 'Clean')), 1)
    ],
    (D, 1, ('Clean', 'Clean', 'Clean', 'Clean')): [
        ((B, 2, ('Clean', 'Clean', 'Clean', 'Clean')), 1),
        ((C, 0, ('Clean', 'Clean', 'Clean', 'Clean')), 1)
    ]
}


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
        return 'State: ' + str(self.STATE) + ' - Path Cost: ' + str(
            self.PATH_COST) + ' - Depth: ' + str(self.DEPTH)


# Search the tree for the goal state and return path from initial state to goal state
def TREE_SEARCH():
    fringe = []
    initial_node = Node(INITIAL_STATE)
    fringe = INSERT(initial_node, fringe)
    while fringe:
        node = REMOVE_NEXT(fringe)  # Get the node with the lowest cost, and remove it from fringe
        if node.STATE == GOAL_STATE:
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
    # queue.append(node)
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
        if queue[i].STATE[1] + queue[i].PATH_COST <= best_fit_node.STATE[
            1] + best_fit_node.PATH_COST:
            best_fit_node = queue[i]
        i += 1

    return queue.pop(i - 1)


# Successor function, mapping the nodes to its successors
def successor_fn(state):  # Lookup list of successor states
    return STATE_SPACE[state]  # successor_fn( 'C' ) returns ['F', 'G']


#####################################
# A STAR VACUUM AGENT
#####################################
Environment = {
    A: 'Dirty',
    B: 'Dirty',
    D: 'Dirty',
    C: 'Dirty',
    'Current': A
}

squareLocationMap = {
    A: {
        B: 'Right',
        C: 'Down'
    },
    B: {
        D: 'Down',
        A: 'Left'
    },
    C: {
        A: 'Up',
        D: 'Right'
    },
    D: {
        B: 'Up',
        C: 'Left'
    }
}


def A_STAR_VACUUM_AGENT(loc_st, path):
    if loc_st[1] == 'Dirty':
        return 'Suck'

    node = path.pop()
    current_loc = loc_st[0]
    new_loc = node.STATE[0]
    return squareLocationMap[current_loc][new_loc]


def Sensors():
    location = Environment['Current']
    return location, Environment[location]


def Actuators(action):
    location = Environment['Current']
    if action == 'Suck':
        Environment[location] = 'Clean'
    else:
        for new_location in squareLocationMap[location]:
            if squareLocationMap[location][new_location] == action:
                Environment['Current'] = new_location


def run():
    path = TREE_SEARCH()
    print('Solution path:')
    for node in path:
        node.display()

    print('---------------------------------------------------')
    print('|       Current      |           New              |')
    print('---------------------------------------------------')
    print('| location    status | action  location    status |')
    print('---------------------------------------------------')
    path.pop()  # Remove init state
    for _ in range((len(path)) * 2):  # every move require a clean
        location, status = Sensors()
        print("| {:12s}{:7s}| ".format(location, status), end='')
        action = A_STAR_VACUUM_AGENT(Sensors(), path)
        Actuators(action)
        location, status = Sensors()
        print("{:8s}{:12s}{:7s}|".format(action, location, status))
    print('---------------------------------------------------')


if __name__ == '__main__':
    run()
