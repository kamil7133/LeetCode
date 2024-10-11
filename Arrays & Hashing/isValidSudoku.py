class Solution:
    def isValidSudoku(self, board):
        return self.CheckSudokuRow(board) and self.CheckSudokuCol(board) and self.CheckSubgrids(board)

    def CheckSudokuRow(self, board):
        for row in board:
            duplicates = set()
            for num in row:
                if num != ".":
                    if num in duplicates:
                        return False
                    duplicates.add(num)
        return True

    def CheckSudokuCol(self, board):
        for col in range(9):
            duplicates = set()
            for row in range(9):
                num = board[row][col]
                if num != ".":
                    if num in duplicates:
                        return False
                    duplicates.add(num)
        return True

    def CheckSubgrids(self, board):
        for row_start in range(0, 9, 3):
            for col_start in range(0, 9, 3):
                duplicates = set()
                for i in range(3):
                    for j in range(3):
                        num = board[row_start + i][col_start + j]
                        if num != '.':
                            if num in duplicates:
                                return False
                            duplicates.add(num)
        return True




# Test
solution = Solution()
print(solution.isValidSudoku(
    [["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]])) #expected true

print(solution.isValidSudoku(
    [["8", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]])) #expected false
