class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows <= 0 or not numRows:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1,1]]
        
        pascals = [[1], [1,1]]
        for i in range(1, numRows-1):
            row = [1]+i*[0]+[1]
            for j in range(i):
                val = pascals[i][j]+pascals[i][j+1]
                row[j+1] = val
            pascals.append(row)
        return pascals
        
