class Solution:
    def __init__(self):
        self.grid = None
        self.max_area = 0

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        self.grid = grid
        
        rows, cols = len(self.grid), len(self.grid[0])

        for row in range(rows):
            for col in range(cols):
                if self.grid[row][col]: # found an island
                    # iterate to find area of island
                    area_of_island = self._dfs(row, col)
                    self.max_area = max(self.max_area, area_of_island)
        
        return self.max_area
    
    def _dfs(self, row, col) -> int:
        # invalid coordinate or water, return
        if row < 0 or row >= len(self.grid) or col < 0 or col >= len(self.grid[0]) or not self.grid[row][col]:
            return 0

        # mark as visited
        self.grid[row][col] = 0 
        
        # iterate neighbours
        return 1 + self._dfs(row+1, col) + self._dfs(row-1, col) + self._dfs(row, col+1) + self._dfs(row, col-1)
