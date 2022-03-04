A = 'A'
B = 'B'

RULE_ACTION = {
    1: 'Suck',
    2: 'Right',
    3: 'Left',
    4: 'NoOp'
}

rules = {
    (A, 'Dirty'): 1,
    (B, 'Dirty'): 1,
    (A, 'Clean'): 2,
    (B, 'Clean'): 3,
    (A, B, 'Clean'): 4
}

Environment = {
    A: 'Dirty',
    B: 'Dirty',
    'Current': A
}


def INTERPRET_INPUT(input):
    return input


def RULE_MATCH(state, rules):
    return rules.get(tuple(state))


def SIMPLE_REFLEX_AGENT(percept):
    state = INTERPRET_INPUT(percept)
    rule = RULE_MATCH(state, rules)
    return RULE_ACTION[rule]


def Sensors():
    location = Environment['Current']
    return location, Environment[location]


def Actuators(action):
    location = Environment['Current']
    if action == 'Suck':
        Environment[location] = 'Clean'
    elif action == 'Right' and location == A:
        Environment['Current'] = B
    elif action == 'Left' and location == B:
        Environment['Current'] = A


def run(n):
    print('---------------------------------------------------')
    print('|       Current      |           New              |')
    print('---------------------------------------------------')
    print('| location    status | action  location    status |')
    print('---------------------------------------------------')
    for i in range(1, n):
        location, status = Sensors()
        print("| {:12s}{:7s}| ".format(location, status), end='')
        action = SIMPLE_REFLEX_AGENT(Sensors())
        Actuators(action)
        location, status = Sensors()
        print("{:8s}{:12s}{:7s}|".format(action, location, status))
    print('---------------------------------------------------')


if __name__ == "__main__":
    run(10)
