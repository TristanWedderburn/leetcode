class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        restaurants = {}
        common = []
        indexSum = len(list1)+len(list2)
        
        for i,a in enumerate(list1):
            restaurants[a] = i
        
        for j,b in enumerate(list2):
            if b in restaurants:
                sum = j+restaurants[b]
                if sum < indexSum:
                    indexSum = sum
                    common = [b]
                elif sum == indexSum:
                    common.append(b)
                
        return common
