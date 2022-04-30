def minmax_decision(state):
    def max_value(state):
        if is_terminal(state):
            return utility_of(state)
        v = -infinity
        for (a, s) in successors_of(state):
            v = max(v, min_value(s))
        # print('V: ' + str(v))
        return v

    def min_value(state):
        if is_terminal(state):
            return utility_of(state)
        v = infinity
        for (a, s) in successors_of(state):
            v = min(v, max_value(s))
        return v

    infinity = float('inf')
    action, state = argmax(successors_of(state), lambda a: min_value(a[1]))
    return action


GOAL = (
    # Diagonal
    (0, 4, 8),
    (2, 4, 6),
    # Top
    (0, 1, 2),
    # Bottom
    (6, 7, 8),
    # First column
    (0, 3, 6),
    # Last column
    (2, 5, 8),
    # Center
    (3, 4, 5),
    (1, 4, 7)
)


def check_win(state, game_piece):
    return any([all([state[index] == game_piece for index in g]) for g in GOAL])


def is_terminal(state):
    """
    returns True if the state is either a win or a tie (board full)
    :param state: State of the checkerboard. Ex: [0; 1; 2; 3; X; 5; 6; 7; 8]
    :return:
    """
    x_count = state.count('X')
    o_count = state.count('O')

    return x_count + o_count >= len(state) or x_count >= 3 \
           and check_win(state, 'X') or o_count >= 3 and check_win(state, 'O')


def utility_of(state):
    """
    returns +1 if winner is X (MAX player), -1 if winner is O (MIN player), or 0 otherwise
    :param state: State of the checkerboard. Ex: [0; 1; 2; 3; X; 5; 6; 7; 8]
    :return:
    """
    if check_win(state, 'X'):
        return 1
    if check_win(state, 'O'):
        return -1
    return 0


def successors_of(state):
    """
    returns a list of tuples (move, state) as shown in the exercise slides
    :param state: State of the checkerboard. Ex: [0; 1; 2; 3; X; 5; 6; 7; 8]
    :return:
    """
    moves = []

    for start_index in range(0, 9):
        if state[start_index] in ['X', 'O']:
            continue

        possible_moves = state.copy()
        if state.count('X') == state.count('O'):
            possible_moves[start_index] = 'X'
        elif state.count('X') > state.count('O'):
            possible_moves[start_index] = 'O'

        moves.append((start_index, possible_moves))

    return moves


def display(state):
    print("-----")
    for c in [0, 3, 6]:
        print(state[c + 0], state[c + 1], state[c + 2])


def main():
    board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    while not is_terminal(board):
        board[minmax_decision(board)] = 'X'
        if not is_terminal(board):
            display(board)
            board[int(input('Your move? '))] = 'O'
    display(board)


def argmax(iterable, func):
    return max(iterable, key=func)


if __name__ == '__main__':
    main()
