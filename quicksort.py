class Solution:
    def quicksort(self, list: List[int], left: int, right: int):
       index = self.partition(list, left, right)
       
       if left < index-1:
          self.quicksort(list, left, index-1)
       if right > index:
          self.quicksort(list, index, right) 
       
    def partition(self, list, left, right):
        pivot = list[left+(right-left)/2]
        while left <= right:
          while list[left] < pivot:
            left+=1
          while list[right]> pivot:
            right-=1
          if left <= right:
            self.swap(list, left, right)
            left+=1
            right-=1
        return left
    
    def swap(self, list, left, right):
        temp = list[right]
        list[right] = list[left]
        list[left] = temp
