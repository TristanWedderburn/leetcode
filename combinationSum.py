class Solution:
    def __init__(self):
        self.combos = set() # unique combos
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        for i in range(len(candidates)): # iterate over each candidate
            candidate = candidates[i]
            self._iterate([candidate], i, candidates, target)
        
        return self.combos

    def _iterate(self, path, i, candidates, target) -> None:
        path_sum = sum(path)
        if path_sum > target:
            return
        if path_sum == target:
            combo = tuple(path) # cast to tuple which is hashable in set
            if combo not in self.combos:
                self.combos.add(combo)
            return

        for j in range(i, len(candidates)): # choose the current or a new candidate
            candidate = candidates[j]
            self._iterate(path + [candidate], j, candidates, target)
