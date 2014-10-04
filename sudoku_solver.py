#https://oj.leetcode.com/problems/sudoku-solver/

'''Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.'''

class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        def canFill(x,y):
            numSet = set('123456789')
            waitingList = []
            for i in range(9):
                waitingList.append(board[x][i])
                waitingList.append(board[i][y])
            for i in range(3):
                for j in range(3):
                    waitingList.append(board[3*(x/3)+i][3*(y/3)+j])
            for i,num in enumerate(waitingList):
                if num!='.' and str(num) in numSet:
                    numSet.remove(str(num))
            if len(numSet)==1:
                return str([i for i in numSet][0])
            else:
                return None

        def check(num,x,y):
            for i in range(9):
                if board[x][i]==str(num) or board[i][y]==str(num):
                    return False
            for i in range(3):
                for j in range(3):
                    if board[3*(x/3)+i][3*(y/3)+j]==str(num):
                        return False
            return True

        def dfs():
            for i in range(9):
                for j in range(9):
                    if board[i][j]=='.':
                        for k in range(1,10):
                            if check(k,i,j):
                            	board[i][j] = str(k)
                            	if dfs():
                            		return True
                            	board[i][j] = '.'
                        return False
            return True
                
        flag = True
        while flag:
            flag = False
            for i in range(9):
                for j in range(9):
                    if board[i][j]=='.':
                        num = canFill(i,j)
                        if num!=None:
                            board[i][j] = num
                            flag = True
        for i in range(9):
            for j in range(9):
                if board[i][j]=='.':
                    flag = True
                    break
        if flag:
            dfs()   
        return board
