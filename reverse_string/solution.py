from typing import List

class Solution:
    def reverse(self, array: List[str]) -> str:
        stack = []
        stack2 = []
        output = ""

        i = 0
        length = len(array)

        for i in range(0, length):
            stack.append(array[i])

        while len(stack) != 0:
            item = stack.pop()
            if item == " ":
                while len(stack2) != 0:
                    elem = stack2.pop()
                    output += elem
                output += item
            else:
                stack2.append(item)
        
        while len(stack2) != 0:
            elem = stack2.pop()
            output += elem

        return output

if __name__ == "__main__":
    #a = "hello, world!"
    a = "whitespaces    4"
    result = Solution().reverse(a)
    print(result)