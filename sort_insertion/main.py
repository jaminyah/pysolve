def insertion_sort(array):
    arraylen = len(array)
    for i in range(1, arraylen):
        j = i
        while array[j - 1] > array[j] and j >= 1:
            # swap a[j] with a[j - 1]
            temp = array[j]
            array[j] = array[j - 1]
            array[j -1] = temp

            # decrement j, 
            # continue the while loop
            j -= 1

    return array

if __name__ == '__main__':
    a = [ 9, 36, 21, 22, 16, 10]
    result = insertion_sort(a)
    print(result)