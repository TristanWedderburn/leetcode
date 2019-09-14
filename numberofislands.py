class Solution:
#     dfs solution is prone to recursion depth error
#     def numIslands(self, grid: List[List[str]]) -> int:
#         if not grid:
#             return 0 #0 islands found
        
#         count = 0
        
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j] == '1':
#                     self.dfs(grid, i, j)
#                     count+=1 
                    
#         return count
    
#     def dfs(self, grid, i, j):
#         if i<0 or j<0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
# #             if i or j are out of bounds or if the value isn't 1, return
#             return
#         else:
#             grid[i][j] = '0' #turn island passed into water for other dfs calls
#             self.dfs(grid, i+1, j)
#             self.dfs(grid, i-1, j)
#             self.dfs(grid, i, j+1)
#             self.dfs(grid, i, j-1)

# bfs solution
    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.bfs(grid, i, j)
                    count += 1
        return count

    def bfs(self, grid, i, j):
        queue = [] #could use collections.deque() 
        queue.append((i, j))
        grid[i][j] = '0'
        while queue:
            directions = [(0,1), (0,-1), (-1,0), (1,0)]
            i, j = queue.pop(0)
            for d in directions:
                nextI = i + d[0]
                nextJ = j + d[1]    
                if nextI >= 0 and nextI < len(grid) and nextJ >= 0 and nextJ< len(grid[0]) and grid[nextI][nextJ] == '1':
                    queue.append((nextI, nextJ))
                    grid[nextI][nextJ] = '0'
