A = 'A'
B = 'B'
C = 'C'
D = 'D'

Environment = {
    A: 'Dirty',
    B: 'Dirty',
    C: 'Dirty',
    D: 'Dirty',
    'Current': A
}


def REFLEX_VACUUM_AGENT(loc_st):
    if loc_st[1] == 'Dirty':
        return 'Suck'

    return 'Right'


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
        action = REFLEX_VACUUM_AGENT(Sensors())
        Actuators(action)
        location, status = Sensors()
        print("{:8s}{:12s}{:7s}|".format(action, location, status))
    print('---------------------------------------------------')


if __name__ == '__main__':
    run(20)
