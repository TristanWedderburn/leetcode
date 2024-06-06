class Solution:
    def __init__(self):
        self.num_of_islands = 0
        self.grid = []

    def numIslands(self, grid: List[List[str]]) -> int:
        # recursively dfs and turn each part into 0s once we've seen it
        # increment counter once we see a one
            
        if not grid:
            return 0
        
        self.grid = grid
        
        row, col = len(self.grid), len(self.grid[0])

        for r in range(row):
            for c in range(col):
                if self.grid[r][c] == "1": # found new island
                    self.num_of_islands+= 1      
                    self._dfs(r, c) # iterate to mark all current island
    
        return self.num_of_islands

    def _dfs(self, row, col) -> int:
        # should not iterate more
        if row < 0 or row == len(self.grid) or col < 0 or col == len(self.grid[0]) or self.grid[row][col] == "0":
            return

        # mark self as visited
        self.grid[row][col] = "0"

        # iterate on neighbours
        self._dfs(row+1, col)
        self._dfs(row-1, col)
        self._dfs(row, col+1)
        self._dfs(row, col-1)
