class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create map
        # iterate through strings and add sorted string as key
        # if key already in there, append to list
        # return all values
        anagram_map = {}

        for s in strs:
            # sort 
            sorted_s = ''.join(sorted(s))

            if sorted_s not in anagram_map:
                anagram_map[sorted_s] = []
            
            anagram_map[sorted_s].append(s)
        
        return [l for l in anagram_map.values()]
