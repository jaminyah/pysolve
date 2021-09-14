def bubble_sort(array):
    arraylen = len(array)

    for i in range(0, arraylen):
        for j in range(arraylen - 1 - i):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
    
    return array

if __name__ == '__main__':
    a = [5, 3, 1, 2, 6, 4]
    result = bubble_sort(a)
    print(result)