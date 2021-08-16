# Move Zeros - Algorithm

Assumption: Input array is mutable. If not, create a mutable array from the input array.

1. Set index i = first index position.
2. Set index j = last index position.
3. While i < j
4. If the element at index i is already zero, increment i.
5. Decrement j until element 0 is found.
6. Swap element at index i with element at index j.
7. Increment index i.
8. Goto instruction 3.
9. Return the array.

## Test Case

input array = [3, 7, 2, 0, 1, 9];

Step - 1: array[i] = 3, array[j] = 9 <br/> 
Step - 2: Since array[j] != 0, decrement j <br/>
Step - 3: array[i] = 3, array[j] = 1 <br/>
Step - 4: Since array[j] != 0, decrement j <br/>
Step - 5: array[i] = 3, array[j] = 0 <br/>
Step - 6: Since array[j] = 0, swap element at index i with element at index j. array[i] = 0, array[j] = 3 <br/>
Step - 7: Increment i, decrement j. array[i] = 7, array[j] = 2 <br/>
Step - 8: Decrement j, index i is not less than index j, return the array. <br/>

<p align="center">
  <img src="https://github.com/jaminyah/drawio/blob/master/movezeros.svg" alt="flowchart" /> 
</p>