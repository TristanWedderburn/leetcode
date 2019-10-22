from collections import deque
class Solution(object):
    def __init__(self):
        self.grid = [[]]
        
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        
        self.grid = grid
        islands = 0
        
        n = len(self.grid)
        m = len(self.grid[0])
        
        for i in range(n):
            for j in range(m):
                if self.grid[i][j]=='1':
                    islands+=1 #found new island
                    self.grid[i][j]='0' #visit
                    
                    island = deque()
                    island.append((i,j))
                    
                    #bfs
                    while island:
                        next = island.popleft()
                        ni = next[0]
                        nj = next[1]
                        
                        if ni+1<n and self.grid[ni+1][nj]=='1':
                            island.append((ni+1,nj))
                            self.grid[ni+1][nj]='0'
                        if ni-1>=0 and self.grid[ni-1][nj]=='1':
                            island.append((ni-1,nj))
                            self.grid[ni-1][nj]='0'
                        if nj+1<m and self.grid[ni][nj+1]=='1':
                            island.append((ni,nj+1))
                            self.grid[ni][nj+1]='0'
                        if nj-1>=0 and self.grid[ni][nj-1]=='1':
                            island.append((ni,nj-1))
                            self.grid[ni][nj-1]='0'

        return islands
