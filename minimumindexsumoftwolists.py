class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        restaurants = {}
        common = []
        indexSum = len(list1)+len(list2)
        
        for i, choices1 in enumerate(list1):
            restaurants[choices1] = i
        
        for j, choices2 in enumerate(list2):
            if choices2 in restaurants:
                sum = j+restaurants[choices2]
                if sum < indexSum:
                    indexSum = sum
                    common = [choices2]
                elif sum == indexSum:
                    common.append(choices2)
                
        return common
