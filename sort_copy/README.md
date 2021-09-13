# Copy Sort 

Algorithm
* Create a empty array named sorted
* Find the smallest element in the input array
* Remove the smallest element from the input array
* Append this element to the sorted array
* Repeat until there are no more elements in the input array

<p align="center">
  <img src="https://github.com/jaminyah/drawio/blob/master/img/sort/sort_copy.svg" alt="sort algo" /> 
</p>

Consider input array = [4, 9, 2, 6, 5] <br/>

end of loop - 1:
input array = [4, 9, 6, 5]
sorted array =  [ 2 ]

end of loop - 2:
input array = [ 9, 6, 5]
sorted array = [ 2, 4 ]

end of loop - 3:
input array = [ 9, 6 ]
sorted array = [ 2, 4, 5 ]

end of loop - 4:
input array = [ 9 ]
sorted array = [ 2, 4, 5, 6 ]

end of loop - 5:
input array = []
sorted array = [ 2, 4, 5, 6, 9]