class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        binary = '{0:032b}'.format(n)
        return int(binary[::-1], base=2)
            
