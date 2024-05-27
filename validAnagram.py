class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # # sort and iterate, nlogn time complexity, constant memory
        # sorted_s = ''.join(sorted(s))
        # sorted_t = ''.join(sorted(t))
        # return sorted_s == sorted_t

        # hashmap of character to count and increment/decrement so they cancel out after iteration
        char_map = {}
        
        if (len(s) != len(t)): # must be same length for valid anagram
            return False
        
        for i in range(len(s)):
            char_map[s[i]] = char_map.get(s[i], 0) + 1
            char_map[t[i]] = char_map.get(t[i], 0) - 1
        
        for val in char_map.values():
            if val != 0:
                return False
        return True
