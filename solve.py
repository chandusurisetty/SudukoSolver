# board = [
#     ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
#     [".", ".", ".", ".", ".", ".", ".", ".", "."],
#     [".", ".", ".", ".", ".", ".", ".", ".", "."],
#     [".", ".", ".", ".", ".", ".", ".", ".", "."],
#     [".", ".", ".", ".", ".", ".", ".", ".", "."],
#     [".", ".", ".", ".", ".", ".", ".", ".", "."],
#     [".", ".", ".", ".", ".", ".", ".", ".", "."],
#     [".", ".", ".", ".", ".", ".", ".", ".", "."],
#     ["9", "8", "7", "5", "6", "4", "3", "2", "1"]
# ]
import time

class Solve:
    def __init__(self,board):
        self.start=time.time()
        self.board=board
        self.N = 9


    def isSafe(self,i, j, x):
        

        # row and column  check
        for r in range(9):
            if self.board[i][r] == x:
                return False
            if self.board[r][j] == x:
                return False
        startRow = i-i % 3
        startCol = j-j % 3
        for row in range(startRow, startRow+3):
            for col in range(startCol, startCol+3):
                if self.board[row][col] == x:
                    return False
        return True


    def solve(self,i=0, j=0):
        self.end=time.time()
        taken=self.end-self.start
        
        if taken>1:
            return False
        

        if i == self.N-1 and j == self.N:
            return True
        if j == self.N:

            return self.solve(i+1, 0)
        if self.board[i][j] != "":

            return self.solve(i, j+1)
        else:
            for x in range(1, self.N+1):
                if self.isSafe(i, j, str(x)):
                    self.board[i][j] = str(x)

                    if self.solve(i, j+1):
                        return True
            self.board[i][j] = ""
        return False


# so=Solve(board)
# if so.solve(0,0):
#     print(so.board)

# else:
#     print("it can't be solved")
