##===============================================
##   Jiadong Mai (20557203)
##   CS 116 Winter 2018
##   Assignment 04, Question 4
##===============================================

import math
import check

# Data definition for Q3 + Q4

# A MineGrid is a (listof (listof Bool))
# Requires:  All lists are non-empty
#            Each (listof Bool) has the same length 

# note: True means mine, False means safe

# A MineBoard is a (listof (listof Str))
# Requires: Each string is either a mine ('*') hidden(' ')
#             or safe (a digit between '0' and '8')
#           All lists are non-empty
#           Each (listof Str) has the same length

# Example board from the assignment file

grid3x3 = [[True ,False,False],
           [False,False,False],
           [False,False,True]]

board3x3 = [[' ', '1', '0'],
            [' ', '2', '1'],
            [' ', ' ', '*']]

board3x3_win = [[' ', '1', '0'],
                ['1', '2', '1'],
                ['0', '1', ' ']]

## Question 4

# game_lost(board) returns true if board contains one or more revealed mines,
#   false otherwise
# game_lost: GameBoard -> Bool

def game_lost(board):
    mined_rows = len(list(filter(lambda row: '*' in row, board)))
    return mined_rows != 0

# line_be_grid_position(lst,b) mutates lst such that each elements in lst is
#   replaced by True or False start from b position
# Effect: lst is mutated
# line_be_grid_position: (listof Str) Nat -> None
# Requires:
# 0 <= b < length of lst
# Example:
# if k = [' ', '1', '0'], then line_be_grid_position(k, 0) is called, k is 
#   now [True, False, False]
def line_be_grid_position(lst,b):   
    if b < len(lst):
        if lst[b] == ' ':
            lst[b] = True
            line_be_grid_position(lst, b+1)
        else:
            lst[b] = False
            line_be_grid_position(lst, b+1)
            
# line_be_grid(lst) return a list of True or False by replacing the element 
#   in lst 
# line_be_grid: (listof Str) -> (listof Bool)
# Example:
# if k = [' ', ' ', '0'], then line_be_grid(k) => [True, True, False]
# if k = ['2', '1', '0'], then line_be_grid(k) => [False, False, False]
def line_be_grid(lst):
    line_be_grid_position(lst, 0)
    return lst

# game_won(grid, board) return True if the game has been won (all safe tiles
#   are revealed and no mine tile), else False
# game_won: MineGrid Gameboard -> Bool
# Examples:
# game_won(grid3x3, board3x3) => False
# game_won(grid3x3, board3x3_win) => False
def game_won(grid,board):
    k = list(map(line_be_grid, board))
    if k == grid:
        return True
    else:
        return False
    
# Tests:
# Test1: Not reveal all the safe or even reveal a mine
board3x3_not_all_safe = [[' ', '1', '0'],
                         [' ', '2', '1'],
                         ['0', '1', ' ']]    
check.expect('Q4T1', game_won(grid3x3, board3x3), False)
check.expect('Q4T2', game_won(grid3x3, board3x3_not_all_safe), False)
# Test2: reveal all the safe and some mine
board3x3_mine = [['*', '1', '0'],
                 ['1', '2', '1'],
                 ['0', '1', ' ']]
check.expect('Q4T3', game_won(grid3x3, board3x3_mine), False)
# Test3: reveal all the safe and no mine
check.expect('Q4T4', game_won(grid3x3, board3x3_win), True)
