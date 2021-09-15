# Run time: O(n*log n)

def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2   # integer division
        left = array[: mid]
        right = array[mid:]

        # recursion
        merge_sort(left)
        merge_sort(right)

        # merge 
        i = 0   # left array index
        j = 0   # right array index
        k = 0   # merged array index

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        # un-merged left array values
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        # un-merged right array values
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
    
    return array
            
if __name__ == '__main__':
    a = [2, 3, 5, 1, 7, 4, 4, 4, 2, 6, 1]
    result = merge_sort(a)
    print(result)