def check_bal(input: str) -> bool:
    
    # w = wing, p = parenthesis, s = square

    balanced = True
    wcount, scount, pcount = 0, 0, 0

    for char in input:
        if char == '{':
            wcount = wcount + 1
        elif char == '[':
            scount = scount + 1
        elif char == '(':
            pcount = pcount + 1
        elif char == '}':
            wcount = wcount - 1
            if wcount < 0:
                balanced = False
                break
        elif char == ']':
            scount = scount - 1
            if scount < 0:
                balanced = False
                break
        elif char == ')':
            pcount = pcount - 1
            if pcount < 0:
               balanced = False
               break

    if wcount != 0 or scount != 0 or pcount != 0:
        balanced = False 
    
    return balanced

if __name__ == '__main__':
       result = check_bal('[{}{})(]')
       print(result)