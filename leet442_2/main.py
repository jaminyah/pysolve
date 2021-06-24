from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        dupl = []

        for num in nums:
            value = abs(num)
            print(f"value = abs(num): {value}")
            if nums[value - 1] < 0:
                dupl.append(value)
            else:
                nums[value - 1] *= -1
                print(f"nums[{value} - 1]: {nums[value - 1]}")

        return dupl

if __name__ == '__main__':
    elements = [2, 5, 2, 1, 1, 4, 3, 11, 4, 6, 8, 11]
    soln = Solution()

    array = soln.findDuplicates(elements)
    print(array)