# Three number sum

## Solution Strategy

* Create three indices, i, j, k
* i - left most index, starting at index 0
* j = i + 1
* k = len(array) - 1, last index
* Set up the equation, A[i] = target - (A[j] + A[k])
* If (A[j] + A[k]) == target, then A[i], A[j], A[k] are solutions 
* If (A[j] + A[k]) > target, set k = k - 1
* If (A[j] + A[k]) < target, set j = j + 1
* For the next loop iteration, set i = i + 1
* Note: if i + 1 == i - 1, continue to increment i to avoid duplicate evaluation.
* i.e. if i > 0 and a[i] == a[i - 1], continue
* Similarly for index j
* i.e. while j < k and A[j] == A[j - 1], j = j + 1

### Case 1: 
A = [1, -1, 0, -2, 2, 4] <br/>
target = 0

Solution, by visual inspection: [-2, 0, 2], [-1, 0, 1]

#### Step 1: 

Sort the input array in ascending order.
[-2, -1, 0, 1, 2, 4]

#### Step 2 - First loop through the array:
Create three indices i, j, k <br/>
i: i = 0 <br/>
j: j = i + 1 <br/>
k: len(array) - 1, the last index in the array

#### Step 3:
The goal is to find three index positions whose sum add to give the target. <br/>
i.e.   A[i] + A[j] + A[k] = target <br/>
Hence, A[i] = target - (A[j] + A[k]) <br/>
Let remainder = (A[j] + A[k]) <br/>

|i|j|k|A[i]|A[j]|A[k]|
|:---|:---|:---|:---|:---|:---|
|0|1|5|-2|-1|4|

For, A[i] = target - (A[j] + A[k]) <br/>
statement 1: -2 = 0 - ( -1 + 4) <br/> 
i.e. sum = ( -1 + 4 ) <br/>

In order for statement 1 to be true remainder must evalutate to 2
so that the equation -2 = 0 - ( 2 ) can be true. <br/>

Since the remainder currently evaluates to ( -1 + 4 ) = 3, set k = k - 1.
Since the array is sorted in ascending order shifting k to the left will result in A[k] having a smaller number value. In this case A[k - 1] = 2 <br/>

k = k - 1 <br/>

|i|j|k|A[i]|A[j]|A[k - 1]|
|:---|:---|:---|:---|:---|:---|
|0|1|5|-2|-1|2|


k = k - 1 <br/>
A[k] = 2 <br/>
So, -2 = 0 - ( -1 + 2 ) <br/>
sum = ( -1 + 2 ) = 1 <br/>
So, 0 - ( 1 ) = -1 which is less that -2 on the left.<br/>

Increment j to increase the remainder <br/> 
j = j + 1 <br/>

|i|j|k|A[i]|A[j + 1]|A[k]|
|:---|:---|:---|:---|:---|:---|
|0|2|5|-2|0|2|

So, -2 = 0 - ( 0 + 2 ) <br/>
sum = ( 0 + 2 ) = 2 <br/>
So, 0 - ( 2 ) = -2 which is equal to the left.<br/>

First solution: <br/>
|i|j|k|A[i]|A[j]|A[k]|
|:---|:---|:---|:---|:---|:---|
|0|1|5|-2|0|2|

[ -2, 0, 2]

#### Step 4 - Second loop through the array:
i: i = 1 <br/>
j: j = i + 1 <br/>
k: len(array) - 1, the last index in the array <br/>

The sorted the input array in ascending array is: <br/>
[-2, -1, 0, 1, 2, 4]

|i|j|k|A[i]|A[j]|A[k]|
|:---|:---|:---|:---|:---|:---|
|1|2|5|-1|0|4|

For, A[i] = target - (A[j] + A[k]) <br/>
-1 = 0 - ( 0 + 4) <br/>
i.e. sum = ( 0 + 4 ) = 4 <br/>

#### Step 5: 
Since sum = (A[j] + A[k]) = ( 0 + 4 ) = 4 is greater than left, - 1 set k = k - 1 so that A[k] = 2, which is a smaller value.

|i|j|k|A[i]|A[j]|A[k]|
|:---|:---|:---|:---|:---|:---|
|1|2|5|-1|0|2|

For, A[i] = target - (A[j] + A[k -1]) <br/>
-1 = 0 - ( 0 + 2) <br/>
i.e. sum = ( 0 + 2 ) = 2 <br/>

Since sum is greater that the left value -1, set k = k - 1 so that A[k] = 1, which is a smaller value.

|i|j|k|A[i]|A[j]|A[k]|
|:---|:---|:---|:---|:---|:---|
|1|2|5|-1|0|1|

For, A[i] = target - (A[j] + A[k -1]) <br/>
-1 = 0 - ( 0 + 1) <br/>
i.e. sum = ( 0 + 1 ) = 1 <br/>

Now, sum = left value, so current values of A[i], A[j], A[k] are a solution set. <br/>
[-1, 0, 1] <br/>

---

# Solution Flowchart

<p align="center">
  <img src="https://github.com/jaminyah/drawio/blob/master/img/3sum/3num_sum.svg" alt="flowchart" /> 
</p>