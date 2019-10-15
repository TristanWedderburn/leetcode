class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
#       brute force, we can use the python library to find the substring needle within haystack. This operation is O(n*m) worst time but frequently O(n)
#       return haystack.find(needle) if len(needle) > 0 else 0
    
        if needle == '':
            return 0
        
        i = 0
        index = -1
        haystackLen = len(haystack)
        needleLen = len(needle)
        
        while(i < haystackLen):
            if haystack[i] == needle[0] and haystackLen-i >= needleLen: #needle can still fit within the remaining string of haystack
                j = 0
                index = i
                while(j < needleLen):
                    if haystack[i+j] != needle[j]: #break early if we can't find the rest of the needle string
                        index = -1
                        break;
                        i=j #move i to j as we have already checked up to i+j
                    j+=1
                if index !=-1: #if we've found the whole string inside haystack, quick return
                    return index
            i+=1
        return index #if we reach here, index should be -1
