def insertion_sort(array):
    for i in range(1, len(array)):
        while array[i - 1] > array[i] and i >= 1:
            # swap a[i] with a[i - 1]
            temp = array[i]
            array[i] = array[i - 1]
            array[i -1] = temp

            # decrement i, 
            # continue the while loop
            i = i - 1

    return array

if __name__ == '__main__':
    a = [ 9, 36, 21, 22, 16, 10]
    result = insertion_sort(a)
    print(result)