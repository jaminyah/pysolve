# Run: python main.py
# Purpose: Move all zeros to the front of the array

from typing import List

def moveZeros(nums: List[int]) -> List[int]:

    length = len(nums)
    i: int = 0
    j: int = length - 1

    # print array on one line
    for num in nums:
        print(num, end=", ")

    print()

    while (i < j):
        if nums[i] == 0:
            print(f"Found at i: {i}")
            i = i + 1
            continue
        
        if nums[j] == 0:
            print(f"Found at j: {j}")
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            i = i + 1
        j = j - 1

    return nums

if __name__ == '__main__':
    array = [0, 9, 11, 8, 0, 1, 0, 5]
    result = moveZeros(array)
    print(result)

 