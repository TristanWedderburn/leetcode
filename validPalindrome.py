class Solution:
    def isPalindrome(self, s: str) -> bool:
        # # convert to lowercase
        # # remove non-alphanumerics

        # # new array, add alphanumerics
        # # iterate over it using two pointers

        # filtered_s = []
        # for char in s:
        #     if (char.isalnum()):
        #         filtered_s.append(char.lower())

        # for i in range(len(filtered_s)):
        #     if (filtered_s[i] != filtered_s[len(filtered_s) - i - 1]):
        #         return False
        # return True

        # use two pointers on each end and keep iterating until right passes left pointer

        left, right = 0, len(s)-1

        while(right >= left):
            left_val = s[left]
            right_val = s[right]

            # check if alphanumeric
            if not left_val.isalnum():
                left+=1
                continue
            elif not right_val.isalnum():
                right-=1
                continue
            
            # must be alphanumeric, check equality
            if left_val.lower() == right_val.lower():
                left+=1
                right-=1
            else:
                return False
            
        return True 
