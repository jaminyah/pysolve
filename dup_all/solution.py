# https://dev.to/effylh/leetcode-442-find-all-duplicates-in-an-array-4a2m

# Method: Use a Set data structure.
#   If the number to be added to the set does not increase the size of the set
#   then the number is a duplicate

from typing import List

class Solution:
    def findAllDuplicates(self, nums: List[int]) -> List[int]:
        
        numSet = set()
        dupl = []

        for num in nums:
            setSize = len(numSet)
            numSet.add(num)

            if setSize == len(numSet):
                dupl.append(num)
                
        if len(dupl) == 0:
            dupl.append(-1)
        
        return dupl