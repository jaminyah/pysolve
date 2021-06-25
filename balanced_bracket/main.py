def balancedBrackets(string):
    
    stack = []
    match = { '[': ']', '{': '}', '(': ')' }
    count = 0

    for elem in string:
        if elem == '[' or elem == '{' or elem == '(':
            stack.append(elem)
            count = count + 1
        elif elem == ']' or elem == '}' or elem == ')':
            if len(stack) > 0:
                item = stack.pop()
                if match[item] == elem:
                    count = count - 1
                else:
                    return False
            else:
                return False
  
    return (count == 0)

if __name__ == '__main__':

    input = ")[]}"
    #input = "[((([])([]){}){}){}([])[]((()))]"
    result = balancedBrackets(input)
    print(result)