from stack import Stack

def check_bal(input: str) -> bool:

    stack = Stack()
    match = {'[':']', '{': '}', '(':')'}
    success = True

    for elem in input:
        if elem == '[' or elem == '{' or elem == '(':
            stack.push(elem)
        elif elem == ']' or elem == '}' or elem == ')':
            item = stack.pop()
            if match[item] == elem:
                continue
            else:
                success = False
                break

    return success

if __name__ == '__main__':
    result = check_bal("[{}{})()]")
    print(result)