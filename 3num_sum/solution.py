# Algo expert success July 2, 2021

from typing import List

class Solution:
    def threeSum(self, a: List[int], target: int) -> List[List[int]]:
    
            """
            i - first index
            j - second index
            k - third index
            """

            output = []
            a.sort()
            length = len(a)

            for i in range(0, length):

                # increment if next element == previous element           
                if i > 0 and a[i] == a[i - 1]:
                    continue

                j = i + 1
                k = length - 1
                element = a[i]
                remainder  = target - element

                while j < k:
                    sum = a[j] + a[k]
                    if sum == remainder:
                        elements = [a[i], a[j], a[k]]
                        output.append(elements)                         # append elements 
                        j = j + 1
                        # increment if next element == previous element
                        while j < k and a[j] == a[j - 1]:
                            j = j + 1
                    elif sum < remainder:
                        j = j + 1
                    else:                                               # sum > remainder:
                        k = k - 1

            return output
