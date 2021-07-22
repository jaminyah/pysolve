from typing import List

class Solution:
    
    def getFirstDuplicate(self, nums: List[int]) -> int:
        
        firstDup = -1
        numSet = set()

        for num in nums:
            size = len(numSet)
            numSet.add(num)

            if size == len(numSet):     # set size has not changed after adding num
                firstDup = num
                break
        
        return firstDup