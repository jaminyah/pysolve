"""
Selection Sort Algorithm
1. Compare element at index 0 with element at index 1
1.1. If element at index 1 is less than element at index 0, swap the elements
1.2. Else, compare element at index 0 with element at index 2 ... array length

2. Compare element at index 1 with element at index 2
2.1. If element at index 2 is less than element at index 1, swap the elements
2.2. Else, compare element at index 1 with element at index 3 ... array length

3. Compare element at index with element at index + 1 until to the array length

Consider, input array = [25, 13, 41, 32, 66, 14, 50]

loop - 1: 
25 and 13 are swapped
a = [13, 25, 41, 32, 66, 14, 50]

loop - 2: 
25 and 14 are swapped
a = [13, 14, 41, 32, 66, 25, 50]

loop - 3: 
41 and 25 are swapped
a = [13, 14, 25, 32, 66, 41, 50]

loop - 4: 
32 needs no swap
a = [13, 14, 25, 32, 66, 41, 50]

loop - 5: 
66 and 41 are swapped
a = [13, 14, 25, 32, 41, 66, 50]

loop - 6: 
66 and 50 are swapped
a = [13, 14, 25, 32, 41, 66, 50]
"""

def selection_sort(array):
    arraylen = len(array)

    for i in range(0, arraylen - 1):
        for j in range(i + 1, arraylen):
            if array[j] < array[i]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
    
    return array

if __name__ == '__main__':
    a = [25, 13, 41, 32, 66, 14, 50]
    result = selection_sort(a)
    print(result)