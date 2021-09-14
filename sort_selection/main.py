"""
Selection Sort Algorithm
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