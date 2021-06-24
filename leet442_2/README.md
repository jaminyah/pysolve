# Leet 442 - Find all duplicates

* Criteria 1 <= a[i] <= n
* For an array with 6 numbers, the smallest numuber can be 1 and the largest 6
* The smallest index = 0 and the largest 5 for a zero based array

* Since the criteria is 1<= a[i] <= n, the provided array starts off with no negative number.
* A negative number means that the formula that was use to create a negative number was previously applied.
i.e. nums[value - 1] *= -1

Pass 1: 

for num in nums:\
    array index = 0\
    value = abs(num): 2\
    nums[2 - 1] = 5                                     # nums[1] = 5\
    nums[2 - 1] *= -1                                   # nums[1] = -5\
    elements = [2, -5, 2, 1, 1, 4, 3, 11, 4, 6, 8, 11]\
\
Pass 2: \

for num in nums:\
    array index = 1\
    value = abs(num): 5\
    nums[5 - 1] = 1                                     # nums[4] = 1\
    nums[4 - 1] *= -1                                   # nums[4] = -1\
    elements = [2, -5, 2, 1, -1, 4, 3, 11, 4, 6, 8, 11]\
\
Pass 3:\

for num in nums:\
    array index = 2\
    value = abs(num): 2\
    nums[2 - 1] = -5                                     # nums[1] = -5\
    elements = [2, -5, 2, 1, -1, 4, 3, 11, 4, 6, 8, 11]\
\
Since the value at index 1 was found to be negative, this means the number 2
was previously found.