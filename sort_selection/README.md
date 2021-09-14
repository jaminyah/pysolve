
Selection Sort Algorithm
1. Compare element at index 0 with element at index 1
1.1. If element at index 1 is less than element at index 0, swap the elements
1.2. Else, compare element at index 0 with element at index 2 ... array length

2. Compare element at index 1 with element at index 2
2.1. If element at index 2 is less than element at index 1, swap the elements
2.2. Else, compare element at index 1 with element at index 3 ... array length

3. Compare element at index with element at index + 1 until to the array length

<p align="center">
  <img src="https://github.com/jaminyah/drawio/blob/master/img/sort/selection_sort.svg" alt="sort algo" /> 
</p>

Consider, input array = [25, 13, 41, 32, 66, 14, 50]

loop - 1: <br/>
25 and 13 are swapped <br/>
a = [13, 25, 41, 32, 66, 14, 50] <br/>

loop - 2: <br/>
25 and 14 are swapped <br/>
a = [13, 14, 41, 32, 66, 25, 50] <br/>

loop - 3: <br/> 
41 and 25 are swapped <br/>
a = [13, 14, 25, 32, 66, 41, 50] <br/>

loop - 4: <br/>
32 needs no swap <br/>
a = [13, 14, 25, 32, 66, 41, 50] <br/>

loop - 5: <br/>
66 and 41 are swapped <br/>
a = [13, 14, 25, 32, 41, 66, 50] <br/>

loop - 6: <br/>
66 and 50 are swapped <br/>
a = [13, 14, 25, 32, 41, 66, 50] <br/>