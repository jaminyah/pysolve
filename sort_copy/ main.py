"""
Reference: Coding for beginners
ISBN: 978-1-84078-642-2
Time complexity: O(n^2)
Space complexity: O(n)
"""

def sort_copy(array):
    copy = array[:]             # slice from first to last index
    sorted = []
    arraylen = len(copy)
    
    while arraylen > 0:         # array len decreases with each iteration
        minIndex = 0
        for currIndex in range(0, arraylen):
            if copy[currIndex] < copy[minIndex]:
                minIndex = currIndex

        sorted.append(copy.pop(minIndex))
        arraylen = len(copy)
    
    return sorted

if __name__ == '__main__':
    a = [4, 9, 2, 6, 5]
    print(sort_copy(a))