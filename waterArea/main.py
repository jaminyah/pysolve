from typing import List

def waterArea(heights: List[int]) -> int:

    maxRh, maxLh = 0, 0         # max height to left and right of current index
    totalArea = 0
    size = len(heights) - 1

    for currIndex, height in enumerate(heights):
        if currIndex > 0 and currIndex < size:
            print(f"currIndex: {currIndex}")
            maxLh = maxLeft(maxLh, currIndex, heights)
            maxRh = maxRight(currIndex, heights)
            currArea = min(maxLh, maxRh) - height

            if currArea > 0:
                totalArea += currArea
    
    return totalArea


def maxLeft(max: int, currIndex: int, heights: List[int]) -> int:

    """
        lh = []
        for i, height in enumerate(heights):
            if i < currIndex:
                lh.append(height)
        
        print(f"max(lh): {max(lh)}")
        return max(lh)
    """
    maxLh = max
    if heights[currIndex - 1] > max:
        maxLh = heights[currIndex - 1]

    print(f"maxLh: {maxLh}")
    return maxLh


def maxRight(currIndex: int, heights: List[int]) -> int:

    rh = []
    for j, height in enumerate(heights):
 
        if j > currIndex:
            rh.append(height)
    
    print(f"max(rh): {max(rh)}")
    return max(rh)


if __name__ == '__main__':
    #hts = [0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]
    #hts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8]
    hts = [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    # hts = [0, 1, 0, 2]
    # hts = [0, 1, 0, 2, 0, 1]
    area = waterArea(hts)
    print(f"area: {area}")