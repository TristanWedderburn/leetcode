from collections import defaultdict 

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        n = len(board)
        
#         using hash table with lists for each row, column and box
#          if n is the rows/columns in the board, O(n) space
#           if n is the number of elements, O(n) as it must run through each index to verify the number
        lookup = defaultdict(list)
        
        for i in range(n):
            lookup['r'+str(i)] = list()
            lookup['c'+str(i)] = list()
            lookup['b'+str(i)] = list()
        
        for j in range(n):
            for k in range(n):
                val = board[j][k]
                if(val != '.'):
                    if val in lookup['r'+str(j)]:
                        return False
                    else:
                        lookup['r'+str(j)].append(val)

                    if val in lookup['c'+str(k)]:
                        return False
                    else:
                        lookup['c'+str(k)].append(val)

                    if val in lookup['b'+str(3*(j//3)+k//3)]:
                        return False
                    else:
                        lookup['b'+str(3*(j//3)+k//3)].append(val)
        return True
        
        
