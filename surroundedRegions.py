class Solution:
    def __init__(self):
        self.board = None

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        self.board = board
        
        rows, cols = len(self.board), len(self.board[0])

        # find all unsurrounded regions and mark them
        # first row, last row, first col, last col
        for row in [0, rows - 1]:
            for col in range(cols):
                if self.board[row][col] == "O":
                    self._capture(row, col)
        
        for row in range(rows):
            for col in [0, cols - 1]:
                if self.board[row][col] == "O":
                    self._capture(row, col)

        # capture all surrounded regions
        # unmark unsurrounded regions 
        for row in range(rows):
            for col in range(cols):
                if self.board[row][col] == "O":
                    self.board[row][col] = "X"
                elif self.board[row][col] == "T":
                    self.board[row][col] = "O"
    
    def _capture(self, row, col) -> None:
        if row < 0 or row >= len(self.board) or col < 0 or col >= len(self.board[0]) or self.board[row][col] != "O":
            return
        
        self.board[row][col] = "T"
        
        self._capture(row + 1, col)
        self._capture(row - 1, col)
        self._capture(row, col + 1)
        self._capture(row , col - 1)
