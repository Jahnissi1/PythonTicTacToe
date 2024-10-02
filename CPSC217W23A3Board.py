# DO NOT EDIT THE FOLLOWING LINES
# COURSE CPSC 217 Winter 2023
# INSTRUCTOR: Jonathan Hudson
# RNkY9dhladt8yUgc1WHi
# DO NOT EDIT THE ABOVE LINES

# TODO: INFORMATION FOR YOUR TA
# Name: Ibuchi Jahnissi Nwakanma
# Student number: 30174827

# This program is composed of 13 functions that helps in playing the the game of X’s and O’s, Tic-Tac-Toe, or Noughts and Crosses
#  Two players are given a square array of size 3,4 or 5 and take turns entering their symbol into the grid.
#  The first one to 3 in a row (across, down, or diagonal) is the winner.

# Constants for the game pieces
EMPTY = 0
X_PIECE = 1
O_PIECE = 2
UP_ONE = 1
UP_TWO = 2
ZERO = 0


#
#  TODO: Insert your implementation of create_board here (code and comments (in-line and above function))
def create_board(rows = 3, columns = 3):

    """The function will take 2 integer parameters in order:rows and columns
    :rows has a default of 3
    :columns has a default of 3
    :returns a two-dimensional list with the indicated number of rows and columns. Every value in the two-dimensional list will be filled an EMPTY constant.
    """

    board = []
    for i in range (rows):
        row = []
        for j in range (columns):
            row.append(EMPTY)
        board.append(row)
    return board


#
#  TODO: Insert your implementation of row_count here (code and comments (in-line and above function))
#
def row_count(board):
    """takes one parameter
    :board
    :return the number of rows
    """
    numrows = len(board)
    return numrows

#
#  TODO: Insert your implementation of column_count here (code and comments (in-line and above function))
#
def column_count(board):
    """takes one parameter your
    :board
    :return the number of columns
    """
    numrows = len(board[ZERO])
    return numrows

#
#  TODO: Insert your implementation of can_play here (code and comments (in-line and above function))
#
def can_play(board,row,column):
    """The function will take 3 parameters in order:
    :board that is 2-dimensiona that holds a representation of the game-state
    :row to look in that is specific to that board
    :column to look in that is specific to that board
    :return True If the location in the board at the given row and given column is EMPTY (or 0), otherwise return False
     """
    board[row][column]
    if board[row][column] == EMPTY:
        return True
    else:
        return False

#
#  TODO: Insert your implementation of play here (code and comments (in-line and above function))
#
def play(board,row,column,piece):
    """The function will take 4 parameters in order:
    :Board a two-dimensional list board that holds a representation of the game-state
    :row to look in that is specific to that board
    :column to look in that is specific to that board
    :piece to play in the indicated location
    :return nothing
    """
    board[row][column] = piece

#
#  TODO: Replace this with your implementation of full here (code and comments (in-line and function))
#
def full(board):
    """The function will take 1 parameter: a two-dimensional list board that holds a representation of the board game-state
    This function is responsible for determining if the game board has any empty(0) locations remaining.
    : board
    :return a boolean value. This value will be True if there are no EMPTY locations in the board,or False if there is at least one EMPTY location remaining in the board.
    """
    for r in range((len(board))):
        for c in range(len((board[ZERO]))):
            mopy = board[r][c]
            if mopy == EMPTY:
                return False
    return True


#  TODO: Insert your implementations of win_in_row (code and comments (in-line and function))
#
def win_in_row(board,row,piece):
    """The function will take 3 parameter:
     :board, a two-dimensional list board that holds a representation of the game-state
     :row to look in that is specific to that board
     :piece type of one of the players
     :return True if there are 3 pieces side by side in the indicated row of the indicated piece type. otherwise false
     """
    for check in range(len(board[row]) - UP_TWO):
        a = (board[row][check])
        b = (board[row][check + UP_ONE])
        c = (board[row][check + UP_TWO])
        cond = (a == piece and b == piece and c == piece)
        if cond:
            return True
    return False
#
#  TODO: Insert your implementations of win_in_column here (code and comments (in-line and function))
#
def win_in_column(board,column,piece):
    """The function will take 3 parameter:
     :board, a two-dimensional list board that holds a representation of the game-state
     :column to look in that is specific to that board
     :piece type of one of the players
     :return True if there are 3 pieces side by side in the indicated row of the indicated piece type. otherwise false
     """
    for check in range(len(board) - UP_TWO):
        a = (board[check][column])
        b = (board[check + UP_ONE][column])
        c = (board[check + UP_TWO][column])
        cond = (a == piece and b == piece and c == piece)
        if cond:
            return True
    return False

#
#  TODO: Insert your implementations of win_in_diagonal_backslash here (code and comments (in-line and function))
#
def win_in_diagonal_backslash(board,piece):
    """These functions will each take 2 parameters:
    :board, a two-dimensional list board that holds a representation of the game-state
    :piece type of one of the players
    :return True if there are 3 pieces in a row in a  backward slash diagonal otherwise false
    """

    for row in range (len(board) - UP_TWO):
        for check in range(len(board[ZERO]) - UP_TWO):

            a = (board[row][check])
            b = (board[row + UP_ONE][check + UP_ONE])
            c = (board[row + UP_TWO][check + UP_TWO])
            cond = (a == piece and b == piece and c == piece)
            if cond:
                return True
    return False



#
#  TODO: Insert your implementations of win_in_diagonal_forward_slash here (code and comments (in-line and function))
#
def win_in_diagonal_forward_slash(board,piece):
    """These functions will each take 2 parameters:
    :board, a two-dimensional list board that holds a representation of the game-state
    :piece type of one of the players
    :return True if there are 3 pieces in a row in a forward slash diagonal otherwise false
    """
    for row in range(len(board)-UP_ONE,UP_ONE,-UP_ONE):
        for check in range(len(board[ZERO]) - UP_TWO):
            a = (board[row][check])
            b = (board[row - UP_ONE][check + UP_ONE])
            c = (board[row -UP_TWO][check + UP_TWO])
            cond = (a == piece and b == piece and c == piece)
            if cond:
                return True
    return False

#
#  TODO: Replace this with your implementation of won here (code and comments (in-line and function))
#
def won(board, piece):
    """The function will take 2 parameters:
    :board, a two-dimensional list board that holds a representation of the game-state
    :piece type of one of the players
    :return True if the player has a win in the board, or False if the player has not won.
    """

    for row in range(len(board)):
        win = win_in_row(board,row,piece)
        if win == True:
            return True
    for columns in range(len(board[ZERO])):
        win = win_in_column(board,columns,piece)
        if win == True:
            return True
    fin = win_in_diagonal_backslash(board, piece)
    if fin == True:
        return True

    lin = win_in_diagonal_forward_slash(board,piece)
    if lin == True:
        return True
    return False


#
#  TODO: Replace this with your implementation of hint here (code and comments (in-line and function))
#
def hint(board, piece):
    """The function will take 2 parameters:
    The following code is an algorithm which gives a hint. It relies on the concept of checking every location in the board.
    :board, a two-dimensional list board that holds a representation of the game-state
    :piece type of one of the players
    :returns a row and a column if there is a hint. Currently there is a default value of -1, -1 which indicates there is no hint.
    """
    for row in range(len(board)):
        for column in range(len(board[ZERO])):
            if can_play(board, row, column) == True:
                play(board,row,column,piece)
                if won(board, piece) == True:
                    play(board,row,column,EMPTY)
                    return row, column
                else:
                    play(board,row,column,EMPTY)
    return -1, -1


##############################################################################
#
# Code below is for testing student functions (IF YOU ARE READING THIS YOU BETTER NO BE CHANGING CODE DOWN HERE)
#
##############################################################################
def game_over(board):
    """
    This function determines if the game is complete due to a win or tie by either player
    :param board: The 2D list board to check
    :return: True if game is complete, False otherwise
    """
    if full(board) or won(board, X_PIECE) or won(board, O_PIECE):
        return True
    return False


if __name__ == '__main__':
    print("File is being run directly so ask about running the tests.")
    if input("Enter Y to run tests:") == "Y":
        from CPSC217W23A3Test import *

        run_tests()
