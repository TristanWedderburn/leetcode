class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:          
        # c = Counter(words)
        # sorted_items = sorted(c.items(), key=lambda item: (-item[1], item[0]))
        # sorted_keys = [item[0] for item in sorted_items]
        # return sorted_keys[:k]

        # bucket sort impl.

        # create map of word to frequency
        c = Counter(words)

        # init list of lists with max len being max frequency of particular word
        freqs = [[] for i in range(len(words))]

        for item in c.items():
            freqs[item[1]].append(item[0])

        output = []
        
        for l in reversed(freqs): # iterate list of lists from back    
            for word in sorted(l):
                if k == 0: # already collected top k
                    break
                
                output.append(word)
                k-=1
            
        return output
