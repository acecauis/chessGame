# Copyright: Jason Maldonado -- 04/05/19
# First version and attempt at making a full Chess Game using Python

# Coding methodology:
#    1) Begin by coding mechanics of each piece
#    2) Code the board structure
#    3) Code game rules
#    4) Code game logging
#    5)  ....
#    6)  ....
import numpy as np

def ChessBoard():
    """
    ChessBoard:  An 8x8 matrix with appropriate indices

    Indices:     ChessBoard notation is A-H (columns) and 1-8 (rows),
                where A2 is equal to the first column of the second row
                (from the bottom)
    """
    board = np.asmatrix([[1] * 8 for i in range(8)])
    return board




ChessBoard
