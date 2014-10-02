#https://oj.leetcode.com/problems/valid-sudoku/

'''Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.'''

class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        for i in range(9):
            #rows
            checkSet = set()
            for j in board[i]:
                if j!='.':
                    if j in checkSet:
                        return False
                    checkSet.add(j)
            #cols
            checkSet = set()
            for j in range(9):
                if board[j][i]!='.':
                    if board[j][i] in checkSet:
                        return False
                    checkSet.add(board[j][i])
        #3*3s
        for i in range(3):
            for j in range(3):
                checkSet = set()
                for x in range(i*3,i*3+3):
                    for y in range(j*3,j*3+3):
                        if board[x][y]!='.':
                            if board[x][y] in checkSet:
                                return False
                            checkSet.add(board[x][y])
        return True
