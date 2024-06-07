class Solution:
    def __init__(self):
        self.coordinates = []
        self.heights = None

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        self.heights = heights
        # algo: start from edges and work in if the height is >= current height

        rows, cols = len(self.heights), len(self.heights[0])

        # init sets for coords that can reach each ocean
        pac_coords = set()
        atl_coords = set()

        # find nodes that can reach pacific, i.e row is 0 or col is 0
        # find nodes that can reach atlantic, i.e row is last and col last

        for i in range(rows):
            self._dfs(i, 0, pac_coords, -1)
            self._dfs(i, cols-1, atl_coords, -1)

        for i in range(cols):
            self._dfs(0, i, pac_coords, -1)
            self._dfs(rows-1, i, atl_coords, -1)

        # return intersection of coords
        return pac_coords & atl_coords
    
    def _dfs(self, row, col, coords, prev_height):
        if (row, col) in coords: # visited
            return
        
        if row < 0 or row >= len(self.heights) or col < 0 or col >= len(self.heights[0]): # invalid coords
            return

        curr_height = self.heights[row][col]
        if curr_height < prev_height: # can't traverse down
            return

        # add to visited set
        coords.add((row, col))
        
        # iterate
        self._dfs(row + 1, col, coords, curr_height)
        self._dfs(row - 1, col, coords, curr_height)
        self._dfs(row, col + 1, coords, curr_height)
        self._dfs(row, col - 1, coords, curr_height)

