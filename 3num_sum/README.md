# Three number sum

## Solution Strategy

### Case 1: 
A = [1, -1, 0, -2, 2, 4] target = 0

Solution, by visual inspection: [-2, 0, 2], [-1, 0, 1]

#### Step 1: 
Sort the input array in ascending order.
[-2, -1, 0, 1, 2, 4]

#### Step 2:
Create three indices i, j, k
* i - initialized to index 0
* j - j = i + 1
* k = len(array) - 1 the last index in the array

#### Step 3:
The goal is to find three index positions whose sum add to give the target. <br/>
i.e.   A[i] + A[j] + A[k] = target <br/>
Hence, A[i] = target - (A[j] + A[k]) <br/>
Let remainder = (A[j] + A[k]) <br/>

#### Code walk through

|i|j|k|A[i]|A[j]|A[k]|
|:---|:---|:---|:---|:---|:---|
|0|1|5|-2|-1|4|


For, A[i] = target - (A[j] + A[k]) <br/>
statement 1: -2 = 0 - ( -1 + 4) 
i.e. remainder = ( -1 + 4 )

In order for statement 1 to be true remainder must evalutate to 2
so that the equation -2 = 0 - ( 2 ) can be true

Since the remainder currently evaluates to ( -1 + 4 ) = 3, set k = k - 1.
Since the array is sorted in ascending order shifting k to the left will result in A[k] having a smaller number value. In this case A[k - 1] = 2

* k = k - 1 <br/>

|i|j|k|A[i]|A[j]|A[k - 1]|
|:---|:---|:---|:---|:---|:---|
|0|1|5|-2|-1|2|


k = k - 1 <br/>
A[k] = 2 <br/>
So, -2 = 0 - ( -1 + 2 ) <br/>
remainder, ( -1 + 2 ) = 1
So, 0 - ( 1 ) = -1 which is less that -2 on the left.<br/>


Increment j to increase the remainder <br/> 
j = j + 1

|i|j|k|A[i]|A[j + 1]|A[k]|
|:---|:---|:---|:---|:---|:---|
|0|1|5|-2|0|2|

So, -2 = 0 - ( 0 + 2 ) <br/>
remainder, ( 0 + 2 ) = 2
So, 0 - ( 2 ) = -2 which is equal to the left.<br/>

First solution: <br/>
|i|j|k|A[i]|A[j]|A[k]|
|:---|:---|:---|:---|:---|:---|
|0|1|5|-2|0|2|

[ -2, 0, 2]