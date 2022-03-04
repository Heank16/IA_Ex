A = 'A'
B = 'B'
C = 'C'
D = 'D'

state = {}
action = None
model = {A: None, B: None, D: None, C: None}

RULE_ACTION = {
    1: 'Suck',
    2: 'Right',
    3: 'Left',
    4: 'NoOp'
}

rules = {
    (A, 'Dirty'): 1,
    (B, 'Dirty'): 1,
    (C, 'Dirty'): 1,
    (D, 'Dirty'): 1,
    (A, 'Clean'): 2,
    (B, 'Clean'): 2,
    (C, 'Clean'): 2,
    (D, 'Clean'): 2,
    (A, B, C, D, 'Clean'): 4
}

Environment = {
    A: 'Dirty',
    B: 'Dirty',
    D: 'Dirty',
    C: 'Dirty',
    'Current': A
}


def INTERPRET_INPUT(input):
    return input


def RULE_MATCH(state, rules):
    return rules.get(tuple(state))


def UPDATE_SATE(state, action, percept):
    location, status = percept
    state = percept
    if all(value == 'Clean' for value in model.values()):
        state = (A, B, C, D, 'Clean')

    model[location] = status

    return state


def REFLEX_AGENT_WITH_STATE(percept):
    global state, action
    state = UPDATE_SATE(state, action, percept)
    rule = RULE_MATCH(state, rules)
    action = RULE_ACTION[rule]
    return action


def Sensors():
    location = Environment['Current']
    return location, Environment[location]


def Actuators(action):
    location = Environment['Current']
    if action == 'Suck':
        Environment[location] = 'Clean'
    elif action == 'Right':
        if location == A:
            Environment['Current'] = B
        elif location == B:
            Environment['Current'] = D
        elif location == D:
            Environment['Current'] = C
        elif location == C:
            Environment['Current'] = A
    elif action == 'Left':
        if location == A:
            Environment['Current'] = C
        elif location == B:
            Environment['Current'] = A
        elif location == D:
            Environment['Current'] = B
        elif location == C:
            Environment['Current'] = D


def run(n):
    print('---------------------------------------------------')
    print('|       Current      |           New              |')
    print('---------------------------------------------------')
    print('| location    status | action  location    status |')
    print('---------------------------------------------------')
    for i in range(1, n):
        location, status = Sensors()
        print("| {:12s}{:7s}| ".format(location, status), end='')
        action = REFLEX_AGENT_WITH_STATE(Sensors())
        Actuators(action)
        location, status = Sensors()
        print("{:8s}{:12s}{:7s}|".format(action, location, status))
    print('---------------------------------------------------')


if __name__ == '__main__':
    run(20)
