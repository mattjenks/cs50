"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = 0
    o_count = 0

    for row in board:
        for cell in row:
            if cell == X:
                x_count += 1
            elif cell == O:
                o_count += 1

    if x_count <= o_count:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()

    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if col == EMPTY:
                possible_actions.add((i, j))

    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise ValueError("Invalid action")

    new_board = copy.deepcopy(board)
    i, j = action
    new_board[i][j] = player(board)

    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    winner = None

    # check rows
    for row in range(3):
        if board[row][0] is not None:
            if board[row][0] == board[row][1] == board[row][2]:
                winner = board[row][0]

    # check columns
    for col in range(3):
        if board[0][col] is not None:
            if board[0][col] == board[1][col] == board[2][col]:
                winner = board[0][col]

    # check diagonals
    if board[1][1] is not None:
        if board[0][0] == board[1][1] == board[2][2]:
            winner = board[0][0]
        elif board[0][2] == board[1][1] == board[2][0]:
            winner = board[0][2]

    return winner

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is None:
        for row in board:
            for col in row:
                if col == EMPTY:
                    return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def maxValue(board):
    if terminal(board):
        return utility(board)
    
    v = -math.inf
    for a in actions(board):
        v = max(v, minValue(result(board, a)))

    return v

def minValue(board):
    if terminal(board):
        return utility(board)
    
    v = math.inf
    for a in actions(board):
        v = min(v, maxValue(result(board, a)))

    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    if player(board) == X:
        #  maximize score for X
        bv = -math.inf
        oa = None;
        for a in actions(board):
            v = max(bv, minValue(result(board, a)))
            if v > bv:
                bv = v
                oa = a
        return oa
    else:
        #  minimize score for O
        bv = math.inf
        oa = None;
        for a in actions(board):
            v = min(bv, maxValue(result(board, a)))
            if v < bv:
                bv = v
                oa = a
        return oa
