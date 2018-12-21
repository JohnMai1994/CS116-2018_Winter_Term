##===============================================
##   Jiadong Mai (20557203)
##   CS 116 Winter 2018
##   Assignment 04, Question 3
##===============================================

import math
import check


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

grid4x4 = [[True,False,False,False,],
           [False,False,False,False],
           [False,False,True,True],
           [True,False,True,False]]

board4x4 = [['','','',''],
            ['','','',''],
            ['','','',''],
            ['','','','']]


## Question 3

# count_mines_no(grid,row,col) returns how many mine tiles are near to the tile at
#   the position row and col in the grid, includes diagonals and itself
# count_mines_no: MineBoard Nat Nat -> None
# requires: grid and board have the same dimensions and are consistent
#           0 <= row < height of board
#           0 <= col < width  of board
# examples:
# count_mines_no(grid4x4,0,0) => 1
# count_mines_no(grid4x4,3,2) => 3
def count_mines_no(grid,row,col):
    row_line = len(grid)-1
    col_line = len(grid[1])
    if row-1 < 0:
        return len(list(filter(lambda s: s== True,grid[row][max(0,col-1):min(col_line,col+2)])))\
               + len(list(filter(lambda s: s== True,grid[min(row_line,row+1)][max(0,col-1):min(col_line,col+2)]))) 
    elif row + 1 > row_line:
        return len(list(filter(lambda s: s== True,grid[max(0,row-1)][max(0,col-1):min(col_line,col+2)])))\
               + len(list(filter(lambda s: s== True,grid[row][max(0,col-1):min(col_line,col+2)])))
    else:    
        return len(list(filter(lambda s: s== True,grid[max(0,row-1)][max(0,col-1):min(col_line,col+2)])))\
               + len(list(filter(lambda s: s== True,grid[row][max(0,col-1):min(col_line,col+2)])))\
               + len(list(filter(lambda s: s== True,grid[min(row_line,row+1)][max(0,col-1):min(col_line,col+2)])))    

# count_mines(grid,row,col) returns how many mine tiles are near to the tile at
#   the position row and col in the grid, includes diagonals
# count_mines: MineBoard Nat Nat -> None
# requires: grid and board have the same dimensions and are consistent
#           0 <= row < height of board
#           0 <= col < width  of board
# examples:
# count_mines(grid4x4,0,1) => 1
# count_mines(grid4x4,3,3) => 3
# count_mines(grid4x4,3,0) => 0
def count_mines(grid,row,col):
    if grid[row][col]:
        return 0
    else:
        return count_mines_no(grid,row,col)
# Test1 for helper function: No Mine surrounded
check.expect('Q3T1H', count_mines(grid3x3,2,0), 0)
check.expect('Q3T2H', count_mines(grid4x4,0,3), 0)
# Test2 for helper funciton: one Mine surrounded
check.expect('Q3T3H', count_mines(grid3x3,1,0), 1)
check.expect('Q3T4H', count_mines(grid4x4,1,0), 1)
check.expect('Q3T5H', count_mines(grid4x4,2,0), 1)
# Test3 for helper function: two or more Mine surrounded
check.expect('Q3T6H', count_mines(grid3x3,1,1), 2)
check.expect('Q3T7H', count_mines(grid4x4,3,1), 3)
check.expect('Q3T8H', count_mines(grid4x4,3,3), 3)
# Test4 for helper function: on Mine
check.expect('Q3T9H', count_mines(grid4x4,0,0), 0)
check.expect('Q3T10H', count_mines(grid4x4, 2,2),0)

# reveal(grid,board, row, col) reveals the tile at the given row and col(umn)
#   in board, using the mine positions from grid
# reveal: MineGrid MineBoard -> None
# requires: grid and board have the same dimensions and are consistent
#           0 <= row < height of board
#           0 <= col < width  of board
# effects: board is mutated
# Examples:
# reveal(grid3x3, board3x3, 0,0) => None, and changes contents of board3x3
# to [['*', '1', '0'], [' ', '2', '1'], [' ', ' ', '*']]
# reveal(grid3x3, board3x3, 1,0) => None, and changes contents of board3x3
# to [[' ', '1', '0'], ['1', '2', '1'], [' ', ' ', '*']]
def reveal(grid,board,row,col):
    if grid[row][col]:
        board[row][col] = '*'
    else:
        board[row][col] = str(count_mines(grid,row,col))
# Tests:
grid3x3 = [[True ,False,False],
           [False,False,False],
           [False,False,True]]

board3x3 = [[' ', '1', '0'],
            [' ', '2', '1'],
            [' ', ' ', '*']]    

# Test1: the position is mine
check.expect('Q3T1', reveal(grid3x3,board3x3,0,0), None)
check.expect('Q3T1(M)', board3x3, [['*', '1', '0'], [' ', '2', '1'],[' ', ' ', '*']])

# Test2: the position is surrounded by 1 mine
check.expect('Q3T2', reveal(grid3x3,board3x3,1,0), None)
check.expect('Q3T2(1)', board3x3, [['*', '1', '0'], ['1', '2', '1'],[' ', ' ', '*']])
check.expect('Q3T3', reveal(grid3x3,board3x3,2,1), None)
check.expect('Q3T3(1)', board3x3, [['*', '1', '0'], ['1', '2', '1'],[' ', '1', '*']])
# Test3: the position is not surrounded by mine
check.expect('Q3T4', reveal(grid3x3,board3x3,2,0), None)
check.expect('Q3T4(None)', board3x3, [['*', '1', '0'], ['1', '2', '1'],['0', '1', '*']])





