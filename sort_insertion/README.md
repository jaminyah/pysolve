# Insertion Sort

Algorithm <br/>

for-loop: i = 1 <br/>

    while-loop is not satisfied 
    so, there is no change
    [9, 36, 21, 22, 16, 10]

for-loop: i = 2 <br/>

    while-loop:
    a[1] > a[2],
    36 is swapped with 21
    [9, 21, 36, 22, 16, 10]


for-loop: i = 3 <br/>

   while-loop:
    a[2] > a[3], <br/>
    36 is swapped with 22 <br/>
    [9, 21, 22, 36, 16, 10] <br/>

for-loop: i = 4 <br/>

    while-loop: <br/>
    a[3] > a[4], <br/>
    36 is swapped with 16 <br/>
    [9, 21, 22, 16, 36, 10] <br/>

    while-loop: <br/>
    a[2] > a[3], <br/>
    22 is swapped with 16 <br/>
    [9, 21, 16, 22, 36, 10] <br/>

    while-loop: <br/>
    a[1]> a[2], <br/>
    21 is swapped with 16 <br/>
    [9, 16, 21, 22, 36, 10] <br/>

for-loop: i = 5 <br/>

    while-loop: <br/>
    a[4] > a[5], <br/>
    36 is swapped with 10 <br/>
    [9, 16, 21, 22, 10, 36] <br/>

    while-loop <br/>
    a[3] > a[4], <br/>
    22 is swapped with 10 <br/>
    [9, 16, 21, 10, 22, 36] <br/>

    while-loop <br/>
    a[2] > a[3] <br/>
    21 is swapped with 10 <br/>
    [9, 16, 10, 21, 22, 36] <br/>

    while-loop <br/>
    a[1] > a[2] <br/>
    16 is swapped with 10 <br/>
    [9, 10, 16, 21, 22, 36] <br/>

Final array <br/>
[9, 10, 16, 21, 22, 36] <br/>